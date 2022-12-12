from pydantic import BaseModel, Field

from ..models import Project
from .spotify import SpotifyMusicSchema


class ReadProjectSchema(BaseModel):
    id: str = Field(..., max_length=Project.MAX_LENGTH_ID, alias="project_id")
    receiver_name: str = Field(..., max_length=Project.MAX_LENGTH_RECEIVER_NAME)
    spotify_music: SpotifyMusicSchema | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class CreateProjectSchema(BaseModel):
    receiver_name: str
