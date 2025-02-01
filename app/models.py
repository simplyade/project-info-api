from pydantic import BaseModel
from pydantic.types import datetime

class BasicInfo(BaseModel):
   email:str
   current_datetime:datetime
   github_url:str
