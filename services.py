import os
import requests

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

TEXT_MODEL = "meta-llama/Llama-3-70b-chat-hf"
IMAGE_MODEL = "black-forest-labs/FLUX.1-schnell"

def generate_design(user_prompt):
    text_response = generate_text_design(user_prompt)
    image_response = generate_image_design(text_response)

    return {
        "design_text": text_response,
        "image_url": image_response
    }

def generate_text_design(prompt):
    url = "https://api.together.xyz/v1/chat/completions"

    payload = {
        "model": TEXT_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a professional fashion designer creating detailed outfit concepts."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    }

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    return data["choices"][0]["message"]["content"]

def generate_image_design(description):
    url = "https://api.together.xyz/v1/images/generations"

    payload = {
        "model": IMAGE_MODEL,
        "prompt": f"fashion design concept, {description}",
        "steps": 30
    }

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    return data["data"][0]["url"]
