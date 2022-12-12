from fastapi import APIRouter

from .health import health_router
from .project import project_router
from .spotify import spotify_router

api_router = APIRouter()
api_router.include_router(project_router, tags=["project"], prefix="/projects")
api_router.include_router(spotify_router, tags=["project"], prefix="/projects")
