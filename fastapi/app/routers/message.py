from app.api import MessageAPI
from app.models import Message, MessageImage
from app.schemas import CreateMessageSchema, ImageMessagesSchema, TextMessagesSchema

from fastapi import APIRouter, Request, Response

message_router = APIRouter()


@message_router.post("/{project_id}/message", response_class=Response)
async def create(
    request: Request, project_id: str, schema: CreateMessageSchema
) -> None:
    await MessageAPI.create(request, project_id, schema)


@message_router.get("/{project_id}/image_messages", response_model=ImageMessagesSchema)
async def get_images(
    request: Request, project_id: str, limit: int = 100
) -> list[MessageImage]:
    return await MessageAPI.get_images(request, project_id, limit)


@message_router.get("/{project_id}/text_messages", response_model=TextMessagesSchema)
async def get_texts(
    request: Request, project_id: str, limit: int = 100
) -> list[Message]:
    return await MessageAPI.get_texts(request, project_id, limit)
