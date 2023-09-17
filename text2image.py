import requests


def query(payload, api):
    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": f"Bearer {api}"}
    payload1 = dict(inputs=payload)
    response = requests.post(API_URL, headers=headers, json=payload1)
    return response.content
