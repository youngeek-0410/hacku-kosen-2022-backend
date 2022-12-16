from typing import Optional

from pydantic import BaseModel, Field

from ..models import Project
from .message import ImageMessagesSchema, TextMessagesSchema


class CreateProjectTopTextSchema(BaseModel):
    top_text: str


class CreateProjectTopImageSchema(BaseModel):
    top_image_url: str


class ReadProjectTopImageSchema(BaseModel):
    url: str


class SpotifyMusicSchema(BaseModel):
    uri: str


class ReadProjectSchema(BaseModel):
    id: str = Field(..., max_length=Project.MAX_LENGTH_ID, alias="project_id")
    receiver_name: str = Field(..., max_length=Project.MAX_LENGTH_RECEIVER_NAME)

    spotify_music: SpotifyMusicSchema | None = None

    top_text: str
    top_image: ReadProjectTopImageSchema | None = None

    text_messages: TextMessagesSchema | None = None
    image_messages: ImageMessagesSchema | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

    @classmethod
    def from_orm(cls, obj: Project | None) -> Optional["ReadProjectSchema"]:  # type: ignore
        if type(obj) is not Project:
            return None

        setattr(
            obj,
            "spotify_music",
            SpotifyMusicSchema(uri=obj.spotify_uri),
        )

        setattr(
            obj,
            "top_image",
            ReadProjectTopImageSchema(url=obj.top_image_url),
        )
        setattr(obj, "top_text", obj.top_text)
        return super().from_orm(obj)


class CreateProjectSchema(BaseModel):
    receiver_name: str


class AllProjectsIdSchema(BaseModel):
    project_ids: list[str]

    class Config:
        orm_mode = True

    @classmethod
    def from_orm(cls, objs: list) -> "AllProjectsIdSchema":  # type: ignore
        return cls(project_ids=[id for id in objs])
