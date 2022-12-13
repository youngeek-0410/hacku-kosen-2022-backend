from app.api import SpotifyMusicAPI
from app.schemas import SpotifyMusicSchema

from fastapi import APIRouter, Request, Response

spotify_music_router = APIRouter()


@spotify_music_router.put(
    "/{project_id}/spotify_music",
    response_class=Response,
)
async def create_spotify_music(
    request: Request, project_id: str, schema: SpotifyMusicSchema
) -> None:
    await SpotifyMusicAPI.put(request, project_id, schema)
