from fastapi import APIRouter, status, HTTPException
from schemas.prompt_schema import PromptSchema
from models.prompt_model import PromptModel


router = APIRouter()


# Get
@router.get("/", status_code=status.HTTP_200_OK, response_model=PromptModel)
async def get_prompt_template():
    pass
    # return sample: {"text": "testando", "last_change_timestamp": "dateasYYYdah:2121:3232"}

# Update
@router.put("/", status_code=status.HTTP_200_OK)
async def update_prompt_template(payload: PromptSchema):
    pass