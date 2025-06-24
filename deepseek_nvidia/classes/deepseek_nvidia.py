import os
from openai import OpenAI
from openai.types.chat import ChatCompletionChunk
from typing import Generator, Optional

class DeepseekNvidia:
    base_url = "https://integrate.api.nvidia.com/v1"
    model = "deepseek-ai/deepseek-r1"

    def __init__(self)->None:
        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.get_api_key()
        )

    def get_api_key(self) -> str:
        api_key = os.getenv("NVIDIA_OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "API key not found. Please set the NVIDIA_OPENAI_API_KEY environment variable."
            )
        return api_key

    def get_response(self, query:str) -> Optional[Generator[ChatCompletionChunk, None, None]]:
        model = self.model
        try:
            return self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": query}],
                temperature=0.6,
                top_p=0.7,
                max_tokens=4096,
                stream=True,
            )
        except Exception as e:
            print(f"Error getting response for query '{query}': {e}")
            return None

    def print_response(self, response:Optional[Generator[ChatCompletionChunk, None, None]]) -> None:
        if response is None:
            print("No response received.")
            return
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

    def print_response_to(self, query:str)->None:
        response = self.get_response(query)
        self.print_response(response)
