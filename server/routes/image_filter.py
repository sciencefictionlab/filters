from fastapi import APIRouter, UploadFile, File

from server.crud.image_filter import make_background_gray
from server.singletons import AppConfig
from fastapi import APIRouter, UploadFile, File

from server.crud.image_filter import make_background_gray
from server.singletons import AppConfig

config = AppConfig.get_config()

router = APIRouter()


@router.post('/upload', response_description="upload file.")
async def _make_background_gray(image: UploadFile = File(...)):
    return await make_background_gray(image)




