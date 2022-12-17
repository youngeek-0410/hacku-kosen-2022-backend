import random
from logging import getLogger

from app.models import Project
from app.schemas import (
    CreateProjectSchema,
    CreateProjectTopTextSchema,
    CreateProjectTopImageSchema,
    SpotifyMusicSchema,
)
from asgiref.sync import sync_to_async
from config.exceptions import NotFoundException

from fastapi import Request

logger = getLogger(__name__)


# FIXME: 使用する頻度に応じて別ファイルに切り出し
def generate_base58_id(length: int) -> str:
    base58_strings = "123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
    return "".join(random.choice(base58_strings) for _ in range(length))


class ProjectAPI:
    @classmethod
    async def get(
        cls,
        request: Request,
        id: str,
        text_messages_limit: int,
        image_messages_limit: int,
    ) -> Project:
        project = await Project.objects.filter(id=id).afirst()
        if not project:
            raise NotFoundException("Project not found.")

        # FIXME: @propertyを使って出来たら嬉しい
        setattr(
            project,
            "text_messages",
            await project.get_text_messages(text_messages_limit),
        )
        setattr(
            project,
            "image_messages",
            await project.get_image_messages(image_messages_limit),
        )
        return project

    @classmethod
    async def put_top_text(
            cls,
            request: Request,
            id: str,
            schema: CreateProjectTopTextSchema,
    ) -> None:
        project = await Project.objects.filter(id=id).afirst()
        if not project:
            raise NotFoundException("Project not found.")

        project.top_text = schema.top_text
        await sync_to_async(project.save)()

    @classmethod
    async def put_top_image(
            cls,
            request: Request,
            id: str,
            schema: CreateProjectTopImageSchema,
    ) -> None:
        project = await Project.objects.filter(id=id).afirst()
        if not project:
            raise NotFoundException("Project not found.")

        project.top_image_url = schema.top_image_url
        await sync_to_async(project.save)()

    @classmethod
    async def put_spotify_uri(
            cls,
            request: Request,
            id: str,
            schema: SpotifyMusicSchema,
    ) -> None:
        project = await Project.objects.filter(id=id).afirst()
        if not project:
            raise NotFoundException("Project not found.")

        project.spotify_uri = schema.uri
        await sync_to_async(project.save)()

    @classmethod
    async def create(cls, request: Request, schema: CreateProjectSchema) -> Project:
        project = await sync_to_async(Project.objects.create)(
            **schema.dict(), id=generate_base58_id(Project.DEFAULT_LENGTH_ID)
        )
        return project

    @classmethod
    async def get_all_project_id(cls, request: Request) -> list:
        projects_id = []
        for project in Project.objects.all():
            if project.receiver_name and project.top_text and project.top_image_url:
                projects_id.append(project.id)
        return projects_id
