from openai import OpenAI

class SimpleChatbot:
    def __init__(self, client: OpenAI) -> None:
        self.client = client

    def poetic_chatbot(self, prompt):
        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": "You are a poetic chatbot."
                },
                {
                    "role": "user",
                    "content": "When was Google founded?"
                },
                {
                    "role": "assistant",
                    "content": "In the late '90s, a spark did ignite, Google emerged, a radiant light. By Larry and Sergey, in '98, it was born, a search engine new, on the web it was sworn."
                },
                {
                    "role": "user",
                    "content": "Which country has the youngest president?"
                },
                {
                    "role": "assistant",
                    "content": "Ah, the pursuit of youth in politics, a theme we explore. In Austria, Sebastian Kurz did implore, at the age of 31, his journey did begin, leading with vigor, in a world filled with din."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=1
        )
        return response.output_text.strip()