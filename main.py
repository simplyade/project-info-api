
from fastapi import FastAPI,Depends
from config import settings
from app.routes import project_info_router
import uvicorn
from fastapi.security import OAuth2PasswordBearer
app = FastAPI(title=settings.API_TITLE, description=settings.API_DESCRIPTION, version=settings.API_VERSION)




app.include_router(project_info_router)

if __name__ =='__main__':
    uvicorn.run(app,host=settings.SERVER_HOST,port=settings.SERVER_PORT)