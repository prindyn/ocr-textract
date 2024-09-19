from fastapi import UploadFile
from app import create_router
from .models import OCRResponse
from .controllers import OCRController


router = create_router()


@router.post("/extract-text", response_model=OCRResponse)
async def extract_text(file: UploadFile):
    return await OCRController.extract_text(file)
