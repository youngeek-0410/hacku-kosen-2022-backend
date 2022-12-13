from logging import getLogger

from asgiref.sync import sync_to_async
from config.exceptions import NotFoundException

from fastapi import Request

from ..models import Project, SpotifyMusic
from ..schemas import SpotifyMusicSchema

logger = getLogger(__name__)


class SpotifyMusicAPI:
    @classmethod
    async def create(
        cls, request: Request, project_id: str, schema: SpotifyMusicSchema
    ) -> SpotifyMusic:
        project = await Project.objects.filter(id=project_id).afirst()
        if not project:
            raise NotFoundException("Project not found")

        spotify_music, _ = await sync_to_async(SpotifyMusic.objects.update_or_create)(
            project=project,
            defaults=dict(
                music_name=schema.name,
                music_external_url=schema.external_url,
                music_preview_url=schema.preview_url,
                music_uri=schema.uri,
                artist_name=schema.artist.name,
                artist_external_url=schema.artist.external_url,
                album_name=schema.album.name,
                album_image_url=schema.album.image_url,
            ),
        )
        return spotify_music
