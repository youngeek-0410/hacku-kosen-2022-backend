from fastapi import APIRouter

from .health import health_router
from .message import message_router
from .project import project_router, spotify_music_router

api_router = APIRouter()
api_router.include_router(project_router, tags=["project"], prefix="/projects")
api_router.include_router(message_router, tags=["message"], prefix="/projects")
api_router.include_router(
    spotify_music_router, tags=["spotify_music"], prefix="/projects"
)
