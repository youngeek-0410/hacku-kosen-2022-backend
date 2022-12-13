from logging import getLogger

from pydantic import BaseModel, Field

from ..models import Message, MessageImage

logger = getLogger(__name__)


class CreateMessageSchema(BaseModel):
    sender_name: str = Field(..., max_length=Message.MAX_LENGTH_SENDER_NAME)
    text: str = Field(..., max_length=Message.MAX_LENGTH_TEXT)
    images: str


class MessageTextSchema(BaseModel):
    text: str
    sender_name: str


class MessageImageSchema(BaseModel):
    url: str
    sender_name: str
    height: int
    width: int


class TextMessagesSchema(BaseModel):
    items: list[MessageTextSchema]
    count: int

    @classmethod
    def from_orm(cls, objs: list[Message]) -> "TextMessagesSchema":
        items = [
            MessageTextSchema(text=message.text, sender_name=message.sender_name)
            for message in objs
        ]
        return cls(items=items, count=len(items))

    class Config:
        orm_mode = True


class ImageMessagesSchema(BaseModel):
    items: list[MessageImageSchema]
    count: int

    @classmethod
    def from_orm(cls, objs: list[MessageImage]) -> "ImageMessagesSchema":
        items = [
            MessageImageSchema(
                url=message_image.image.url,
                sender_name=message_image.message.sender_name,
                height=message_image.image.height,
                width=message_image.image.width,
            )
            for message_image in objs
        ]
        return cls(items=items, count=len(items))

    class Config:
        orm_mode = True
