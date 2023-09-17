from PIL import Image
import io
import requests


def query(payload, api):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
    headers = {"Authorization": f"Bearer {api}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


image_bytes = query({
    "inputs": 'tiger as astronutetus, illustration by tim burton',
})

image = Image.open(io.BytesIO(image_bytes))

image.show()
