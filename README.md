# Auto installer : https://www.patreon.com/posts/auto-runpod-for-89919157 - use this until a tutorial
# Modified to be working on Windows by Furkan Gözükara - SECourses
## https://www.youtube.com/SECourses
## https://www.patreon.com/SECourses
## https://www.twitter.com/GozukaraFurkan
## SDXL Background Replacement for Product Images

---
title: SDXL Background Replacement for Product Images
emoji: 🖼️
colorFrom: green
colorTo: purple
sdk: gradio
sdk_version: 3.43.2
app_file: app.py
pinned: true
---

# SDXL Background Replacement for Product Images

Building an online store requires lots of high quality product and marketing images. This is an early demo of a background replacement tool built with Stable Diffusion XL that makes it easy to use your existing product images to make something new. Please be patient during peak demand. 😅

To use it, upload your product photo and describe the background you’d like to see in place of the original. Optionally, describe what you don’t want in the negative prompt field.

<center>
  <video width="512" height="512" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/64e678b09cb7c83a9d72241c/nHdQpjHXtZQ9lDXGreyGs.mp4"></video>
</center>

## More information

You can check our FAQs below! We are also gathering resources from the community and sharing ideas in the [Community](https://huggingface.co/spaces/Shopify/background-replacement/discussions) tab. Shopify is on a mission to redefine commerce with AI. If you’re an AI or ML engineer looking to build the future of commerce, [join us](https://www.shopify.com/careers)!

## FAQs

1. **What is the purpose of this Space?** This is a preview of our background replacement tool for product imagery built with Stable Diffusion XL. Access to innovative text-to-image solutions will transform the possibilities for millions of merchants. We’re releasing an early demo to learn from the community.
2. **Can I use the demo for commercial usage?** The demo is a preview and isn’t intended for production use, but the source is available and there is no commercial use restriction in the license.
3. **What data is Shopify collecting?** Shopify isn’t collecting any usage data from this Space. We’re sharing this demo because we’re excited to bring these technologies to merchants and hope to get there faster with direct feedback from the community. We look forward to hearing from you!
4. **I got a weird image, can I report it or send it to you?** Absolutely! We appreciate your help in identifying any issues or anomalies. Please report any strange or unexpected results with the image and relevant details in the community channel. It will help us refine and improve the tool for future users.
5. **Are there any limitations to the demo?** This tool is currently in its early stages and you may hit edge cases that don’t function as intended. Share these examples with us. We appreciate your patience and feedback as we work to improve the technology!
6. **What are the system requirements to run the background replacement demo?** If you’d like to run the Space on your own GPU it can be run on an NVIDIA T4 Medium but we recommend the NVIDIA A10G Small for improved stability and performance.
7. **When will this feature be available on Shopify?** We’re releasing an early demo on Hugging Face to refine and enhance the technology based on valuable feedback from the community. While we can't provide an exact launch date just yet, keep an eye out for updates as we approach the official launch. 


# pip freeze info

```
Microsoft Windows [Version 10.0.19045.3448]
(c) Microsoft Corporation. All rights reserved.

G:\bg_replace\background-replacement\venv\Scripts>activate

(venv) G:\bg_replace\background-replacement\venv\Scripts>pip freeze
absl-py==2.0.0
accelerate==0.23.0
addict==2.4.0
aiofiles==23.2.1
altair==5.1.1
annotated-types==0.5.0
anyio==3.7.1
attrs==23.1.0
basicsr==1.4.2
cachetools==5.3.1
certifi==2023.7.22
charset-normalizer==3.2.0
click==8.1.7
colorama==0.4.6
contourpy==1.1.1
cycler==0.11.0
diffusers==0.21.2
exceptiongroup==1.1.3
facexlib==0.3.0
fastapi==0.103.1
ffmpy==0.3.1
filelock==3.12.4
filterpy==1.4.5
fonttools==4.42.1
fsspec==2023.9.2
future==0.18.3
gfpgan==1.3.8
google-auth==2.23.1
google-auth-oauthlib==1.0.0
gradio==3.45.1
gradio_client==0.5.2
grpcio==1.58.0
h11==0.14.0
httpcore==0.18.0
httpx==0.25.0
huggingface-hub==0.17.3
idna==3.4
imageio==2.31.4
importlib-metadata==6.8.0
importlib-resources==6.1.0
Jinja2==3.1.2
jsonschema==4.19.1
jsonschema-specifications==2023.7.1
kiwisolver==1.4.5
lazy_loader==0.3
llvmlite==0.41.0
lmdb==1.4.1
Markdown==3.4.4
MarkupSafe==2.1.3
matplotlib==3.8.0
mpmath==1.3.0
networkx==3.1
numba==0.58.0
numpy==1.25.2
oauthlib==3.2.2
opencv-python==4.8.0.76
orjson==3.9.7
packaging==23.1
pandas==2.1.1
Pillow==10.0.1
platformdirs==3.10.0
protobuf==4.23.4
psutil==5.9.5
pyasn1==0.5.0
pyasn1-modules==0.3.0
pydantic==2.4.1
pydantic_core==2.10.1
pydub==0.25.1
pyparsing==3.1.1
python-dateutil==2.8.2
python-multipart==0.0.6
pytz==2023.3.post1
PyWavelets==1.4.1
PyYAML==6.0.1
realesrgan==0.3.0
referencing==0.30.2
regex==2023.8.8
requests==2.31.0
requests-oauthlib==1.3.1
rpds-py==0.10.3
rsa==4.9
safetensors==0.3.3
scikit-image==0.21.0
scipy==1.11.2
semantic-version==2.10.0
six==1.16.0
sniffio==1.3.0
starlette==0.27.0
sympy==1.12
tb-nightly==2.15.0a20230927
tensorboard-data-server==0.7.1
tifffile==2023.9.26
timm==0.9.7
tokenizers==0.13.3
tomli==2.0.1
toolz==0.12.0
torch==2.0.1+cu118
torchvision==0.15.2+cu118
tqdm==4.66.1
transformers==4.33.2
typing_extensions==4.8.0
tzdata==2023.3
urllib3==2.0.5
uvicorn==0.23.2
websockets==11.0.3
Werkzeug==2.3.7
xformers==0.0.21
yapf==0.40.2
zipp==3.17.0

(venv) G:\bg_replace\background-replacement\venv\Scripts>
```
