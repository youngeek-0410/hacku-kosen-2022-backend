import base64
import binascii
import io
import zipfile
from logging import getLogger

from asgiref.sync import sync_to_async
from config.exceptions import BadRequestException, NotFoundException
from django.core.files.images import ImageFile

from fastapi import Request

from ..models import Message, MessageImage, Project
from ..schemas import CreateMessageSchema

logger = getLogger(__name__)


class MessageAPI:
    @classmethod
    async def create(
        cls, request: Request, project_id: str, schema: CreateMessageSchema
    ) -> None:
        project = await Project.objects.filter(id=project_id).afirst()
        if not project:
            raise NotFoundException("Project not found")

        message = await sync_to_async(Message.objects.create)(
            project=project, sender_name=schema.sender_name, text=schema.text
        )

        try:
            image_zip_binary = base64.b64decode(schema.images)
        except binascii.Error:
            raise BadRequestException("Invalid base64 string")

        try:
            image_zip = zipfile.ZipFile(io.BytesIO(image_zip_binary))
        except zipfile.BadZipFile:
            raise BadRequestException("Invalid zip file")

        message_images = []
        for file_name in image_zip.namelist():
            message_images.append(
                MessageImage(
                    image=ImageFile(image_zip.open(file_name, "r")), message=message
                )
            )
        await MessageImage.objects.abulk_create(message_images)

    @classmethod
    async def get_texts(
        cls, request: Request, project_id: str, limit: int
    ) -> list[Message]:
        project = await Project.objects.filter(id=project_id).afirst()
        if not project:
            raise NotFoundException("Project not found")

        return await project.get_text_messages(limit)

    @classmethod
    async def get_images(
        cls, request: Request, project_id: str, limit: int
    ) -> list[MessageImage]:
        project = await Project.objects.filter(id=project_id).afirst()
        if not project:
            raise NotFoundException("Project not found")

        return await project.get_image_messages(limit)
