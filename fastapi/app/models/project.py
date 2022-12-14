from django.db import models

from .base import TimestampModelMixin
from .message import Message, MessageImage
from .spotify import SpotifyMusic


class Project(TimestampModelMixin):
    MAX_LENGTH_ID = 32
    DEFAULT_LENGTH_ID = 7
    id = models.CharField(max_length=MAX_LENGTH_ID, primary_key=True, editable=False)

    MAX_LENGTH_RECEIVER_NAME = 32
    receiver_name = models.CharField(max_length=MAX_LENGTH_RECEIVER_NAME)

    MAX_LENGTH_TOP_TEXT = 32
    top_text = models.CharField(default="", max_length=MAX_LENGTH_TOP_TEXT)

    MAX_LENGTH_URL = 256
    top_image_url = models.URLField(default="", max_length=MAX_LENGTH_URL)

    def __str__(self) -> str:
        return f"Project for {self.receiver_name} [{self.id}]"

    async def get_spotify_music(self) -> SpotifyMusic | None:
        return await SpotifyMusic.objects.filter(project=self).afirst()

    async def get_text_messages(self, limit: int) -> list["Message"]:
        return [
            obj
            async for obj in Message.objects.filter(project=self)
            .order_by("-created_at")
            .all()
        ][:limit]

    async def get_image_messages(self, limit: int) -> list["MessageImage"]:
        return [
            obj
            async for obj in MessageImage.objects.filter(message__project=self)
            .order_by("-created_at")
            .all()
        ][:limit]
