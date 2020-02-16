class Message:
    def __init__(
        self, app, text: str, message_id: int, from_id: int, created_at: int
    ):
        self.app = app
        self.text = text
        self.message_id = message_id
        self.from_id = from_id
        self.created_at = created_at

    async def answer(self, text):
        return await self.app.api_method(
            "messages/send", {"text": text, "to": self.from_id}
        )
