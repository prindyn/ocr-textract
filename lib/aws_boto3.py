import os
import boto3

textract = None


def init_textract_client():
    """
    Initializes a Textract client using the AWS credentials.

    Returns:
        boto3.client: A Textract client object.

    Raises:
        None

    Notes:
        - This function uses the `boto3` library to create a Textract client.
        - The AWS credentials are retrieved from the environment variables:
            - `AWS_ACCESS_KEY_ID`: The AWS access key ID.
            - `AWS_SECRET_ACCESS_KEY`: The AWS secret access key.
            - `AWS_DEFAULT_REGION`: The region name for the Textract client.
    """
    return boto3.client(
        'textract',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION')
    )


try:
    textract = init_textract_client()
except Exception as e:
    print(f"Failed to initialize Textract client: {e}")
