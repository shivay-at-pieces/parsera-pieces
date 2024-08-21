from pieces_copilot_sdk import PiecesClient
from parsera.utils import singleton

@singleton
class PiecesModel:
    def __init__(self, *args, **kwargs):
        config = {
            'baseUrl': 'http://localhost:1000'  # Replace with your actual Pieces OS URL
        }
        self.pieces_client = PiecesClient(config)

    async def ainvoke(self, messages):
        if isinstance(messages, str):
            prompt = messages
        else:
            prompt = "\n".join([f"{msg.type}: {msg.content}" for msg in messages])
        response = self.pieces_client.ask_question(prompt)
        return response
