import requests

import base64

base64_images = {}

with open("image_0.jpg", "rb") as f:
    base64_images[0] = base64.b64encode(f.read()).decode()
with open("image_1.jpg", "rb") as f:
    base64_images[1] = base64.b64encode(f.read()).decode()

invoke_url = "https://ai.api.nvidia.com/v1/retrieval/nvidia/nemotron-3.5-rerank-8b/reranking"

headers = {
    "Authorization": "Bearer $NVIDIA_AI_API_KEY",
    "Accept": "application/json",
}

payload = {
    "model": "nvidia/nemotron-3.5-rerank-8b",
    "query": {
        "text": "How is AI improving the intelligence and capabilities of robots?"
    },
    "passages": [
        {
            "text": "AI enables robots to perceive, plan, and act autonomously."
            , "image": f"data:image/jpeg;base64,{base64_images[0]}"
            
        },
        {
            "text": "A biological foundation model designed to analyze and generate DNA, RNA, and protein sequences."
            , "image": f"data:image/jpeg;base64,{base64_images[1]}"
            
        }
    ]
}

session = requests.Session()
response = session.post(invoke_url, headers=headers, json=payload)

response.raise_for_status()
response_body = response.json()
print(response_body)
