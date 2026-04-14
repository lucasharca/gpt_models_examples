from openai import OpenAI

class TextGenerator:
    def __init__(self, client: OpenAI) -> None:
        self.client = client

    def generate_text(self, prompt, max_tokens = 16, temperature=0.7):
        client = self.client
        response = client.responses.create(
            model="gpt-4.1-mini", 
            input=prompt,
            max_output_tokens=max_tokens,
            temperature=temperature
        )

        return response.output_text

   