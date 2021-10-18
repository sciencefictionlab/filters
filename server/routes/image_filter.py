from pathlib import Path

from fastapi import APIRouter, Body, UploadFile, File
from starlette.responses import FileResponse

from server.crud.image_filter import upload_image_and_filter
from server.singletons import AppConfig
import shutil
config = AppConfig.get_config()

router = APIRouter()


@router.post('/upload', response_description="upload file.")
async def _upload_image_and_filter(image: UploadFile = File(...)):
    return await upload_image_and_filter(image)




