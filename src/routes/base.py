from fastapi import FastAPI, APIRouter, Depends
import os
from helpers.config import get_setings,Settings

base_router = APIRouter(
    prefix='/api/v1',
    tags=["api_v1"]
)

@base_router.get("/")

async def welcome(app_settings:Settings=Depends(get_setings)):

    app_name=app_settings.APP_NAME
    app_version=app_settings.APP_VERSION
    return {"Application Name": app_name,"Application Version": app_version}