from pydantic import BaseModel, Field
from typing import Optional, Dict

class ImageRequest(BaseModel):
    prompt: str = Field(..., description="Text description for image generation")
    version_of_model: str = Field(..., description="Version of the model to fine-tune")
    input_params: Optional[Dict[str, str]] = Field(None, description="Optional parameters like image size, etc.")

class ImageResponse(BaseModel):
    image_url: str = Field(..., description="URL of the generated image")

