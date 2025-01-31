from fastapi import APIRouter
from app.models import ProjectInfo

project_info_router = APIRouter()

@project_info_router.get("/project-info", response_model=ProjectInfo)
async def read_project_info():
    project_info = ProjectInfo(
        project_description="This is a simple API that provides information about a project.",
        api_documentation={
            "endpoint_url": "https://api.example.com/project-info",
            "request_format": "None",
            "response_format": "JSON"
 },
        job_posting="https://hng.tech/hire/python-developers"
    )
    return project_info