import requests
from langchain_core.language_models import BaseLLM


class QianFanModel(BaseLLM):
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def _call(self, prompt: str, stop: list = None):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }
        payload = {
            'prompt': prompt,
            # 根据通义千问的API文档配置请求参数
            'max_tokens': 100,
            'temperature': 0.7,
        }
        response = requests.post(f"{self.base_url}", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()['choices'][0]['text']

    def invoke(self, messages):
        # 将messages转换为适当的prompt格式
        prompt = "\n".join([msg.content for msg in messages])
        return self._call(prompt)
