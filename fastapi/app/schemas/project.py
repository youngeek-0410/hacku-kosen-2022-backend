from pydantic import BaseModel, Field

from ..models import Project


class ReadProjectSchema(BaseModel):
    id: str = Field(..., max_length=Project.MAX_LENGTH_ID, alias="project_id")
    receiver_name: str = Field(..., max_length=Project.MAX_LENGTH_RECEIVER_NAME)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class CreateProjectSchema(BaseModel):
    receiver_name: str
