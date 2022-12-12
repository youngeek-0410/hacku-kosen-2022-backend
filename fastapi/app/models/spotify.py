from django.db import models

from .base import TimestampModelMixin


class SpotifyMusic(TimestampModelMixin):
    MAX_LENGTH_URL = 256
    MAX_LENGTH_NAME = 256

    project = models.ForeignKey("Project", on_delete=models.CASCADE)

    music_name = models.CharField(max_length=MAX_LENGTH_NAME)
    music_external_url = models.URLField(max_length=MAX_LENGTH_URL)
    music_preview_url = models.URLField(max_length=MAX_LENGTH_URL)

    artist_name = models.CharField(max_length=MAX_LENGTH_NAME)
    artist_external_url = models.URLField(max_length=MAX_LENGTH_URL)

    album_name = models.CharField(max_length=MAX_LENGTH_NAME)
    album_image_url = models.URLField(max_length=MAX_LENGTH_URL)

    def __str__(self) -> str:
        return f"SpotifyMusic[{self.music_name}] ({self.project})"
