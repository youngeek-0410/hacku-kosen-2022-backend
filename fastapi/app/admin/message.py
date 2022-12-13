from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.safestring import mark_safe

from ..models import Message, MessageImage


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):  # type: ignore
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(
                f'<a href="{image_url}" target="_blank">'
                f'<img src="{image_url}" alt="{file_name}" width="100" height="100"'
                f'style="object-fit: cover;"/></a>'
            )

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe("".join(output))


class ImageInline(admin.TabularInline):
    model = MessageImage
    extra = 0
    formfield_overrides = {models.ImageField: {"widget": AdminImageWidget}}


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "sender_name",
        "text",
        "project",
    )
    ordering = ("-created_at",)
    search_fields = ("receiver_name", "text", "project")

    inlines = [ImageInline]
