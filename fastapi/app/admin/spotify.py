from django.contrib import admin

from ..models import SpotifyMusic


@admin.register(SpotifyMusic)
class SpotifyMusicAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "music_name",
        "music_external_url",
        "music_preview_url",
        "uri",
        "artist_name",
        "artist_external_url",
        "album_name",
        "album_image_url",
    )
    ordering = ("project",)
    search_fields = ("project", "music_name",)
