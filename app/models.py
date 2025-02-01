from pydantic import BaseModel
from pydantic.types import datetime

class BasicInfo(BaseModel):
   email:str
   current_timezone:datetime
   github_url:str