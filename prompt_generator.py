"""
# **Prompt generator for text to image** using  API inference of **hugging face**
"""

import requests


def query(payload, api):
    API_URL = "https://api-inference.huggingface.co/models/succinctly/text2image-prompt-generator"
    headers = {"Authorization": f"Bearer {api}"}
    payload1 = dict(inputs=payload)
    response = requests.post(API_URL, headers=headers, json=payload1)
    return response.json()[0]["generated_text"]
