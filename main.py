from fastapi import FastAPI, HTTPException, status
from models import ImageRequest, ImageResponse
from services import replicate_generate_image

app = FastAPI(
    title="Replicate Image Generation API",
    description="API for fine-tuning and generating images using the Replicate API",
    version="1.0.0"
)

@app.post(
    "/generate-image/",
    response_model=ImageResponse,
    status_code=status.HTTP_200_OK
)
async def generate_image(request: ImageRequest):
    """
    Endpoint to fine-tune a model and generate an image.

    - **prompt**: The text description for generating the image.
    - **version_of_model**: The version of the model to use.
    - **input_params**: Additional parameters like image size, style, etc.

    Returns the URL of the generated image.
    """
    try:
        image_url = await replicate_generate_image(request.prompt, request.version_of_model, request.input_params)
        return ImageResponse(image_url=image_url)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

