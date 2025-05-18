import requests


def infer_response(question: str, model: str) -> str:
    url = "http://localhost:11434/api/generate"

    data = {
        "model": model,
        "prompt": question,
        "stream": False,
    }
    response = requests.post(url, json=data, timeout=3600)
    if response.status_code == 200:
        return str(response.json()["response"]).strip()

    raise ValueError(response.status_code)
