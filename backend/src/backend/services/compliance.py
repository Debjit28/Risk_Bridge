import os
import requests
from dotenv import load_dotenv

load_dotenv()

NVIDIA_KEY = os.getenv("NVIDIA_AI_API_KEY")
RERANK_URL = "https://ai.api.nvidia.com/v1/retrieval/nvidia/nemotron-3.5-rerank-8b/reranking"

# Hardcoded controls for our first test
SAMPLE_CONTROLS = [
    {"id": "NIST-AC-2", "text": "Account management: The organization manages information system accounts, including establishing, activating, modifying, reviewing, disabling, and removing accounts."},
    {"id": "ISO-A.12.1.2", "text": "Change management: Changes to the organization, business processes, information processing facilities and systems that affect information security shall be controlled."},
    {"id": "NIST-SI-7", "text": "Software, firmware, and information integrity: The organization employs integrity verification tools to detect unauthorized changes to software and information."}
]

def analyze_wazuh_event(event_description: str):
    """
    Takes a Wazuh alert description and finds the most relevant NIST/ISO control.
    """
    headers = {
        "Authorization": f"Bea
        "Accept": "application/json",
    }

    # Format the hardcoded conucture NVIDIA wants
    passages = [{"text": control["text"]} for control in SAMPLE_CONTROLS]

    payload = {
        "model": "nvidia/nemot
        "query": {"text": event_description},
        "passages": passages
    }

    response = requests.post(RERANK_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return {"error": "NVIDsponse.text}

    rankings = response.json()

    # Map back to our sample c
    results = []
    for rank in rankings:
        idx = rank["index"]
        results.append({
            "control_id": SAMPLE_CONTROLS[idx]["id"],
            "score": rank["log
            "description": SAMPLE_CONTROLS[idx]["text"]
        })

    return results