from app.api import ProjectAPI
from app.models import Project
from app.schemas import CreateProjectSchema, ReadProjectSchema

from fastapi import APIRouter, Request

project_router = APIRouter()


@project_router.get("/{project_id}", response_model=ReadProjectSchema)
async def get(request: Request, project_id: str) -> Project:
    return await ProjectAPI.get(request, project_id)


@project_router.post(
    "/",
    response_model=ReadProjectSchema,
)
async def create(request: Request, schema: CreateProjectSchema) -> Project:
    return await ProjectAPI.create(request, schema)
