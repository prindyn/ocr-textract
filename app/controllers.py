from fastapi import UploadFile
from .models import OCRResponse
from .services import (
    remove_file,
    upload_file,
    extract_text_from_image
)


class OCRController:

    @staticmethod
    async def extract_text(file: UploadFile):
        image_path = await upload_file(file)
        extracted_text = await extract_text_from_image(image_path)
        await remove_file(file)
        return OCRResponse(extracted_text=extracted_text)
