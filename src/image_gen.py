import streamlit as st
import requests
import io
from PIL import Image

api_key=st.secrets.HUGGINGFACEHUB_API_TOKEN

# API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": f"Bearer {api_key}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        st.error("Error: " + str(response.status_code) + " " + response.text)
        return None

def img_gen(prompt):
    image_bytes = query({"inputs": prompt})
    return image_bytes

# decoded_img = img_gen("boss baby dancing in the rain")

# image = Image.open(io.BytesIO(decoded_img))

# save_path = "generated_image.png"
# image.save(save_path)


