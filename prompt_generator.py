# **Prompt generator for text to image** using  API inference of **hugging face**


import requests

API_URL = "https://api-inference.huggingface.co/models/succinctly/text2image-prompt-generator"
headers = {"Authorization": f"Bearer {API KEY}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

x=input()

output = query({
	"inputs": x ,
})
output[0]['generated_text']
