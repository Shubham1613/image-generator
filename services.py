import httpx
import os
from config import REPLICATE_API_URL, REPLICATE_API_TOKEN

async def replicate_generate_image(
        prompt: str,
        model_version: str,
        input_params: dict
) -> str:

    """
    Interacts with Replicate's API to generate images.

    :param prompt: Description of the image to generate.
    :param model_version: Version of the model used for fine-tuning.
    :param input_params: Additional input parameters for the image generation.
    :return: URL of the generated image.
    """

    headers = {
        "Authorization": f"Token {REPLICATE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "version": model_version,
        "input": {
            "prompt": prompt,
            **(input_params or {})
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(REPLICATE_API_URL, json=payload, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Error from Replicate API: {response.text}")

        result = response.json()
        return result['output'][0]  # Assuming the URL is the first output

