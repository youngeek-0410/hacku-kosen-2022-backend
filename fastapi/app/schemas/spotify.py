from pydantic import BaseModel, Field


class ReadSpotifyArtistSchema(BaseModel):
    name: str
    external_url: str

    class Config:
        orm_mode = True


class CreateSpotifyArtistSchema(BaseModel):
    name: str
    external_url: str


class ReadSpotifyAlbumSchema(BaseModel):
    name: str
    image_url: str

    class Config:
        orm_mode = True


class CreateSpotifyAlbumSchema(BaseModel):
    name: str
    image_url: str


class ReadSpotifyMusicSchema(BaseModel):
    music_name: str
    music_external_url: str
    music_preview_url: str
    uri: str
    artist_name: str
    artist_external_url: str
    album_name: str
    album_image_url: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class CreateSpotifyMusicSchema(BaseModel):
    name: str
    external_url: str
    preview_url: str
    uri: str
    artist: CreateSpotifyArtistSchema
    album: CreateSpotifyAlbumSchema
