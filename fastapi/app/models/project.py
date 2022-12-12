from django.db import models

from .base import TimestampModelMixin
from .spotify import SpotifyMusic


class Project(TimestampModelMixin):
    MAX_LENGTH_ID = 32
    DEFAULT_LENGTH_ID = 7
    id = models.CharField(max_length=MAX_LENGTH_ID, primary_key=True, editable=False)

    MAX_LENGTH_RECEIVER_NAME = 32
    receiver_name = models.CharField(max_length=MAX_LENGTH_RECEIVER_NAME)

    def __str__(self) -> str:
        return f"Project for {self.receiver_name} [{self.id}]"

    async def get_spotify_music(self) -> SpotifyMusic | None:
        return await SpotifyMusic.objects.filter(project=self).afirst()
