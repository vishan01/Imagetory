import requests
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
headers = {"Authorization": "Bearer {api_key}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": 'tiger as astronutetus, illustration by tim burton' ,
})

import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

image.show()
