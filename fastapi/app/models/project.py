from django.db import models

from .base import TimestampModelMixin


class Project(TimestampModelMixin):
    MAX_LENGTH_ID = 32
    DEFAULT_LENGTH_ID = 7
    id = models.CharField(max_length=MAX_LENGTH_ID, primary_key=True, editable=False)

    MAX_LENGTH_RECEIVER_NAME = 32
    receiver_name = models.CharField(max_length=MAX_LENGTH_RECEIVER_NAME)

    def __str__(self) -> str:
        return f"Project for {self.receiver_name} [{self.id}]"
