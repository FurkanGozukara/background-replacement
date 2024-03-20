import os
import gradio as gr
from background_replacer import replace_background
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--share", action='store_true')
args = parser.parse_args()
developer_mode = os.getenv('DEV_MODE', True)

DEFAULT_POSITIVE_PROMPT = "on the pavement, poolside, idyllic infinity pool, Hawaiian hilltops, commercial product photography"
DEFAULT_NEGATIVE_PROMPT = ""

EXAMPLES = [
    [
        "examples/black-sneakers-with-white-sole.jpg",
        "on the grass in Central Park, gorgeous summer day with Bethesda fountain in the background, commercial footwear product photography",
        "people, litter, trash, crowds, messy",
    ],
    [
        "examples/DIY-beard-balm.jpg",
        "on a mossy rock, white wood anemone blossoms, Loch Ken, Scotland",
        "purple, wrong proportions",
    ],
    [
        "examples/dj-making-music-on-mixer.jpg",
        "on the turntables with a packed dance floor, epic midnight edm party in Miami Beach, colorful nightlife photography",
        "disfigured, dismembered, mangled, marred",
    ],
    [
        "examples/a-man-jeans.jpg",
        "on the beach in Malibu, a five-star beachfront hotel in the background, stark late afternoon light near the dunes, lifestyle photography",
        "blurry background, ripples, soft focus, bokeh",
    ],
]

INTRO = """
# Modified to be working on Windows by Furkan Gözükara - SECourses
## https://www.youtube.com/SECourses - https://www.patreon.com/SECourses

To use it, upload your product photo (.jpg or .png), then describe the background you’d like to see in place of the original. For best results follow the general pattern in the examples below:
1. ❌ _Do not_ describe your product in the prompt (ex: black sneakers)
2. ✅ Do describe the "grounding" for your product (ex: placed on a table)
3. ✅ Do describe the scene you want (ex: in a greek cottage)
4. ✅ Do describe a style of image (ex: side view commercial product photography)
5. 🤔 Optionally, describe what you want to avoid 🙅 in the negative prompt field
"""

MORE_INFO = """
### More information
- You can check our [FAQs here](https://huggingface.co/spaces/Shopify/background-replacement/blob/main/README.md#faqs)!
- We are also gathering resources from the community and sharing ideas [here](https://huggingface.co/spaces/Shopify/background-replacement/discussions).
- Shopify is on a mission to redefine commerce with AI. If you’re an AI or ML engineer looking to build the future of commerce, [join us](https://www.shopify.com/careers)!
"""

def generate(
    image,
    positive_prompt,
    negative_prompt,
    seed,
    depth_map_feather_threshold,
    depth_map_dilation_iterations,
    depth_map_blur_radius,
	num_inference_steps,
	num_images_per_prompt,
	controlnet_conditioning_scale,
	guidance_scale,
	num_images_to_generate,
    progress=gr.Progress(track_tqdm=True)
):
    if image is None:
        return [None, None, None, None]

    options = {
        'seed': seed,
        'depth_map_feather_threshold': depth_map_feather_threshold,
        'depth_map_dilation_iterations': depth_map_dilation_iterations,
        'depth_map_blur_radius': depth_map_blur_radius,
		'num_inference_steps' : num_inference_steps,
		'num_images_per_prompt' : num_images_per_prompt,
		'controlnet_conditioning_scale' : controlnet_conditioning_scale,
		'guidance_scale' : guidance_scale,
		'num_images_to_generate' : num_images_to_generate,
    }

    return replace_background(image, positive_prompt, negative_prompt, options)

custom_css = """
    #image-upload {
        flex-grow: 1;
    }
    #params .tabs {
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }
    #params .tabitem[style="display: block;"] {
        flex-grow: 1;
        display: flex !important;
    }
    #params .gap {
        flex-grow: 1;
    }
    #params .form {
        flex-grow: 1 !important;
    }
    #params .form > :last-child{
        flex-grow: 1;
    }
    .md ol, .md ul {
        margin-left: 1rem;
    }
    .md img {
        margin-bottom: 1rem;
    }
"""

with gr.Blocks(css=custom_css) as iface:
    gr.Markdown(INTRO)

    with gr.Row():
        with gr.Column():
            image_upload = gr.Image(
                label="Product image",
                type="pil",
                elem_id="image-upload"
            )
            caption = gr.Label(
                label="Caption",
                visible=developer_mode
            )
        with gr.Column(elem_id="params"):
            with gr.Tab('Prompts'):
                positive_prompt = gr.Textbox(
                    label="Positive Prompt: describe what you'd like to see",
                    lines=3,
                    value=DEFAULT_POSITIVE_PROMPT
                )
                negative_prompt = gr.Textbox(
                    label="Negative Prompt: describe what you want to avoid",
                    lines=3,
                    value=DEFAULT_NEGATIVE_PROMPT
                )
            if developer_mode:
                with gr.Tab('Options'):
                    num_inference_steps = gr.Slider(precision=0,minimum=1, maximum=300,value=30, default=30,step=1, label="Num Inference Steps")
                    num_images_per_prompt = gr.Slider(precision=0,minimum=1, maximum=100,value=1, default=1,step=1, label="Batch Size - Uses More VRAM")
                    controlnet_conditioning_scale = gr.Slider(precision=0,minimum=0.1,value=0.65, maximum=2.0, step=0.01, default=0.65, label="ControlNet Conditioning Scale")
                    guidance_scale = gr.Slider(precision=0,minimum=1.0, maximum=30.0,value=10.0, step=0.5, default=10.0, label="Guidance Scale")
                    num_images_to_generate = gr.Slider(precision=0,minimum=1,value=1, maximum=10000, default=1,step=1, label="Number of Images to Generate")
  
                    seed = gr.Number(
                        label="Seed",
                        precision=0,
                        value=-1,
                        elem_id="seed",
                        visible=developer_mode
                    )
                    depth_map_feather_threshold = gr.Slider(
                        label="Depth map feather threshold",
                        value=128,
                        minimum=0,
                        maximum=255,
                        visible=developer_mode
                    )
                    depth_map_dilation_iterations = gr.Number(
                        label="Depth map dilation iterations",
                        precision=0,
                        value=10,
                        minimum=0,
                        visible=developer_mode
                    )
                    depth_map_blur_radius = gr.Number(
                        label="Depth map blur radius",
                        precision=0,
                        value=10,
                        minimum=0,
                        visible=developer_mode
                    )
            else:
                seed = gr.Number(value=-1, visible=True, label="Seed")
                depth_map_feather_threshold = gr.Slider(
                    value=128, visible=True,label="Depth map feather threshold" )
                depth_map_dilation_iterations = gr.Number(
                    precision=0, value=10, visible=True,label="Depth map dilation iterations")
                depth_map_blur_radius = gr.Number(
                    precision=0, value=10, visible=True,label="Depth map blur radius")

    gen_button = gr.Button(value="Generate!", variant="primary")

    with gr.Tab('Results'):
        results = gr.Gallery(
            show_label=True,
            object_fit="contain",
            columns=4
        )

    if developer_mode:
        with gr.Tab('Generated'):
            generated = gr.Gallery(
                show_label=True,
                object_fit="contain",
                columns=4
            )

        with gr.Tab('Pre-processing'):
            pre_processing = gr.Gallery(
                show_label=True,
                object_fit="contain",
                columns=4
            )
    else:
        generated = gr.Gallery(visible=True)
        pre_processing = gr.Gallery(visible=True)

    gr.Examples(
        examples=EXAMPLES,
        inputs=[image_upload, positive_prompt, negative_prompt],
    )

    gr.Markdown(MORE_INFO)

    gen_button.click(
        fn=generate,
        inputs=[
            image_upload,
            positive_prompt,
            negative_prompt,
            seed,
            depth_map_feather_threshold,
            depth_map_dilation_iterations,
    depth_map_blur_radius,
	num_inference_steps,
	num_images_per_prompt,
	controlnet_conditioning_scale,
	guidance_scale,
	num_images_to_generate
			
        ],
        outputs=[
            results,
            generated,
            pre_processing,
            caption
        ],
    )

iface.queue(api_open=False).launch(show_api=False,inbrowser=True,share=args.share)
