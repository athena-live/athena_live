"""WebSocket consumers for the messaging app."""
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class MessagingConsumer(AsyncJsonWebsocketConsumer):
    """Echo consumer placeholder."""

    async def connect(self) -> None:
        await self.accept()
        await self.send_json({"message": "connected"})

    async def receive_json(self, content, **kwargs) -> None:
        await self.send_json({"echo": content})

    async def disconnect(self, code) -> None:
        await super().disconnect(code)
