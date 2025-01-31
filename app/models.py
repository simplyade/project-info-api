from pydantic import BaseModel

class ProjectInfo(BaseModel):
    project_description: str
    api_documentation: dict
    job_posting: str
