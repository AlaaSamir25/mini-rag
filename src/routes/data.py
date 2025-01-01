from fastapi import FastAPI, APIRouter, Depends,UploadFile
from helpers.config import get_setings,Settings
from controllers import DataCController
data_router = APIRouter(
    prefix='/api/v1/data',
    tags=["api_v1","data"]
)
@data_router.post("/upload/{project_id}")
async def upload_data(project_id:str,file:UploadFile,
                      app_settings:Settings=Depends(get_setings)):
    

    is_valid=DataCController().validate_uploaded_file(file=file)
    return is_valid
    
