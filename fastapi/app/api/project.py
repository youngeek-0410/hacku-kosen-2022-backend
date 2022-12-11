import random
from logging import getLogger

from app.models import Project
from app.schemas import CreateProjectSchema
from asgiref.sync import sync_to_async
from config.exceptions import NotFoundException

from fastapi import Request

logger = getLogger(__name__)


# FIXME: 使用する頻度に応じて別ファイルに切り出し
def generate_base58_id(length: int) -> str:
    BASE58_STRINGS = "123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
    return "".join(random.choice(BASE58_STRINGS) for _ in range(length))


class ProjectAPI:
    @classmethod
    async def get(cls, request: Request, id: str) -> Project:
        project = await Project.objects.filter(id=id).afirst()
        if not project:
            raise NotFoundException("Project not found.")
        return project

    @classmethod
    async def create(cls, request: Request, schema: CreateProjectSchema) -> Project:
        return await sync_to_async(Project.objects.create)(
            **schema.dict(), id=generate_base58_id(Project.DEFAULT_LENGTH_ID)
        )
