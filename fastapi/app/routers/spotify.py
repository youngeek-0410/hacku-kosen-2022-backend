from ..api import SpotifyMusicAPI
from ..models import SpotifyMusic
from ..schemas import ReadSpotifyMusicSchema, CreateSpotifyMusicSchema

from fastapi import APIRouter, Request

spotify_router = APIRouter()


@spotify_router.post(
    "/{project_id}/spotify_music",
    response_model=ReadSpotifyMusicSchema,
)
async def create(request: Request, schema: CreateSpotifyMusicSchema, project_id: str) -> SpotifyMusic:
    return await SpotifyMusicAPI.create(request, schema, project_id)
