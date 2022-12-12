from app.api import ProjectAPI, SpotifyMusicAPI
from app.models import Project, SpotifyMusic
from app.schemas import CreateProjectSchema, ReadProjectSchema, SpotifyMusicSchema

from fastapi import APIRouter, Request

project_router = APIRouter()


@project_router.get("/{project_id}", response_model=ReadProjectSchema)
async def get(request: Request, project_id: str) -> Project:
    return await ProjectAPI.get(request, project_id)


@project_router.post(
    "/",
    response_model=ReadProjectSchema,
)
async def create(request: Request, schema: CreateProjectSchema) -> Project:
    return await ProjectAPI.create(request, schema)


@project_router.post(
    "/{project_id}/spotify_music",
    response_model=SpotifyMusicSchema,
)
async def create_spotify_music(
    request: Request, project_id: str, schema: SpotifyMusicSchema
) -> SpotifyMusic:
    return await SpotifyMusicAPI.create(request, project_id, schema)
