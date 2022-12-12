from django.contrib import admin

from ..models import SpotifyMusic


@admin.register(SpotifyMusic)
class SpotifyMusicAdmin(admin.ModelAdmin):
    list_display = (
        "music_name",
        "project",
        "music_external_url",
        "music_preview_url",
        "artist_name",
        "artist_external_url",
        "album_name",
        "album_image_url",
    )
    ordering = ("-updated_at",)
    search_fields = ("project", "music_name")
