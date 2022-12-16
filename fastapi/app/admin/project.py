from django.contrib import admin

from ..models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "receiver_name",
        "top_text",
        "top_image_url",
        "spotify_uri",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)
    search_fields = ("id", "receiver_name")
