import requests
from typing import List, Dict

class GatewayLLMClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "X-Gateway-API-Key": api_key,
            "Content-Type": "application/json"
        }

    def list_models(self):
        resp = requests.get(
            f"{self.base_url}/v1/models",
            headers=self.headers
        )
        resp.raise_for_status()
        return resp.json()["data"]

    def chat(self, model: str, messages: List[Dict[str, str]]) -> str:
        payload = {
            "model": model,
            "messages": messages
        }

        resp = requests.post(
            f"{self.base_url}/v1/chat/completions",
            headers=self.headers,
            json=payload,
            timeout=60
        )
        
        
        if resp.status_code != 200:
            print("Gateway error:", resp.status_code, resp.text)
            return "Error del modelo al generar respuesta."

        return resp.json()["choices"][0]["message"]["content"]

    def embeddings(self, model: str, text: str, dimensions: int = 512):
        payload = {
            "model": model,
            "input": text,
            "dimensions": dimensions
        }

        resp = requests.post(
            f"{self.base_url}/v1/embeddings",
            headers=self.headers,
            json=payload,
            timeout=90
        )
        resp.raise_for_status()

        return resp.json()["data"][0]["embedding"]