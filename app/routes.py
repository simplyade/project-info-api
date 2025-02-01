from fastapi import APIRouter
from app.models import BasicInfo
from datetime import datetime
import pytz

project_info_router = APIRouter()
#Email Address
email ="adebisioluseye250@gmail.com"
#GitHUB repository URL
github_url = "https://github.com/simplyade/myrepo"


@project_info_router.get("/", response_model=BasicInfo)
async def read_project_info():
    current_datetime =datetime.now(pytz.utc).isoformat(timespec='milliseconds')
    
    try:
        basic_info = BasicInfo(
            email= email,
            current_timezone =current_datetime,
            github_url=github_url
                 )
        
        return basic_info.dict(exclude_none=True)
    except Exception as e:
        return {"error":str(e)}
        
    