from logging import getLogger
from typing import Optional

from pydantic import BaseModel

from ..models import SpotifyMusic

logger = getLogger(__name__)


class SpotifyArtistSchema(BaseModel):
    name: str
    external_url: str


class SpotifyAlbumSchema(BaseModel):
    name: str
    image_url: str


class SpotifyMusicSchema(BaseModel):
    name: str
    external_url: str
    preview_url: str
    artist: SpotifyArtistSchema
    album: SpotifyAlbumSchema

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

    @classmethod
    def from_orm(cls, obj: SpotifyMusic | None) -> Optional["SpotifyMusicSchema"]:  # type: ignore
        if type(obj) is not SpotifyMusic:
            return None

        setattr(
            obj,
            "artist",
            SpotifyArtistSchema(
                name=obj.artist_name,
                external_url=obj.artist_external_url,
            ),
        )
        setattr(
            obj,
            "album",
            SpotifyAlbumSchema(name=obj.album_name, image_url=obj.album_image_url),
        )
        setattr(obj, "name", obj.music_name)
        setattr(obj, "external_url", obj.music_external_url)
        setattr(obj, "preview_url", obj.music_preview_url)
        return super().from_orm(obj)
