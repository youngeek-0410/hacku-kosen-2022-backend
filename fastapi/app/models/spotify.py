from django.db import models

from .base import TimestampModelMixin
from .project import Project


class SpotifyMusic(TimestampModelMixin):
    DEFAULT_LENGTH_ID = 7
    MAX_LENGTH_ID = 32
    MAX_URL_ID = 255
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    music_name = models.CharField(max_length=MAX_LENGTH_ID, primary_key=True, editable=False)
    music_external_url = models.URLField(max_length=MAX_URL_ID)
    music_preview_url = models.URLField(max_length=MAX_URL_ID)
    uri = models.CharField(max_length=MAX_LENGTH_ID)

    artist_name = models.CharField(max_length=MAX_LENGTH_ID)
    artist_external_url = models.URLField(max_length=MAX_URL_ID)

    album_name = models.CharField(max_length=MAX_LENGTH_ID)
    album_image_url = models.URLField(max_length=MAX_URL_ID)

    def __str__(self) -> str:
        return f"{self.music_name} registered in the project [{self.id}]"
