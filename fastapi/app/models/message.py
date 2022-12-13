from django.db import models

from .base import TimestampModelMixin


def upload_to_message_image(instance: "MessageImage", filename: str) -> str:
    return f"message_images/{instance.message.project.id}/{filename}"


class Message(TimestampModelMixin):
    MAX_LENGTH_SENDER_NAME = 32
    sender_name = models.CharField(max_length=MAX_LENGTH_SENDER_NAME)

    MAX_LENGTH_TEXT = 256
    text = models.CharField(max_length=MAX_LENGTH_TEXT)

    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        related_name="messages",
    )


class MessageImage(TimestampModelMixin):
    image = models.ImageField(upload_to=upload_to_message_image)

    message = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="images",
    )
