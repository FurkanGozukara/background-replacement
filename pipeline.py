import torch
import os
from diffusers import StableDiffusionXLControlNetPipeline, ControlNetModel, AutoencoderKL, UniPCMultistepScheduler

pipe = None


def init():
    global pipe

    print("Initializing depth ControlNet...")

    depth_controlnet = ControlNetModel.from_pretrained(
        "diffusers/controlnet-depth-sdxl-1.0",
        use_safetensors=True,
        torch_dtype=torch.float16
    ).to("cuda")

    print("Initializing autoencoder...")

    vae = AutoencoderKL.from_pretrained(
        "madebyollin/sdxl-vae-fp16-fix",
        torch_dtype=torch.float16,
    ).to("cuda")

    print("Initializing SDXL pipeline...")

    pipe = StableDiffusionXLControlNetPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        controlnet=[depth_controlnet],
        vae=vae,
        variant="fp16",
        use_safetensors=True,
        torch_dtype=torch.float16
        # low_cpu_mem_usage=True
    ).to("cuda")

    pipe.enable_model_cpu_offload()
    # speed up diffusion process with faster scheduler and memory optimization
    pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)
    # remove following line if xformers is not installed
    pipe.enable_xformers_memory_efficient_attention()


import os
import datetime

def run_pipeline(image, positive_prompt, negative_prompt, seed, num_inference_steps=30, num_images_per_prompt=4, controlnet_conditioning_scale=0.65, guidance_scale=10.0, num_images_to_generate=1):
    if seed == -1:
        print("Using random seed")
        generator = None
    else:
        print("Using seed:", seed)
        generator = torch.manual_seed(seed)

    all_generated_images = []
    for count in range(num_images_to_generate):
        images = pipe(
        prompt=positive_prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=num_inference_steps,
        num_images_per_prompt=num_images_per_prompt,
        controlnet_conditioning_scale=controlnet_conditioning_scale,
        guidance_scale=guidance_scale,
        generator=generator,
        image=image
        ).images

        all_generated_images.extend(images)  # Add the generated images to the list

        # Print progress
        print(f"Generated {count + 1} of {num_images_to_generate}")

    # Saving images to outputs folder

    return all_generated_images


