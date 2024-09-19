import os
import easyocr
from typing import List, Dict
from fastapi import UploadFile, HTTPException

reader = easyocr.Reader(['en'])


async def upload_file(file: UploadFile) -> str:
    image_path = f'uploads/{file.filename}'
    try:
        with open(image_path, 'wb') as f:
            f.write(await file.read())
    except Exception as e:
        raise IOError(f"Faile uploading file: {image_path} ({str(e)})")
    else:
        return image_path


async def remove_file(file: UploadFile) -> bool:
    try:
        image_path = f'uploads/{file.filename}'
        if os.path.exists(image_path):
            os.remove(image_path)
    except Exception as e:
        return False
    else:
        return True


async def extract_text_from_image(image_path: str) -> List[Dict[str, float]]:
    try:
        results = reader.readtext(image_path)
        extracted_text = [{"text": text, "confidence": prob}
                          for (_, text, prob) in results]
        return extracted_text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
