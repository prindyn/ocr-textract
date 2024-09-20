import os
import time
from typing import List, Dict
from fastapi import UploadFile
from lib.aws_boto3 import textract
from botocore.exceptions import EndpointConnectionError


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
        job_status = ""
        extracted_text = []

        if not os.path.exists(image_path):
            raise FileExistsError(f"File not found: {image_path}")

        with open(image_path, "rb") as f:
            image = f.read()

        while job_status != 200:
            response = textract.detect_document_text(
                Document={'Bytes': image}
            )
            job_status = response['ResponseMetadata']['HTTPStatusCode']
            if job_status != 200:
                time.sleep(5)

        if job_status == 200:
            for block in response['Blocks']:
                if block['BlockType'] == 'LINE':
                    extracted_text.append(
                        {"text": block['Text'], "confidence": block['Confidence']})

        return extracted_text
    except EndpointConnectionError as e:
        raise Exception(f"Exception while connecting to AWS Textract: {str(e)}")
    except Exception as e:
        raise Exception(f"Exception while extracting text: {str(e)}")
