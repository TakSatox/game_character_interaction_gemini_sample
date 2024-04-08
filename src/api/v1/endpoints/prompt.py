from fastapi import APIRouter, status, HTTPException
from crud.prompt_spec import PromptSpec
from schemas.prompt_schema import PromptSchema
from models.prompt_model import PromptModel, ResponseUpdatePromptModel
from core.errors_handling.models.not_found import NotFoundModel



# Router Decorator
router = APIRouter()

# Get
@router.get("/", status_code=status.HTTP_200_OK, response_model=PromptModel, responses={
    status.HTTP_404_NOT_FOUND: {
        "model": NotFoundModel
    }
})
async def get_prompt_template():
    prompts = PromptSpec()
    prompt = prompts.get_prompt()
    if prompt:
        return prompt
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The 'prompts' collection is empty or does not exist")

# Update
@router.put("/", status_code=status.HTTP_200_OK, response_model=ResponseUpdatePromptModel)
async def update_prompt_template(payload: PromptSchema):
    prompts = PromptSpec()
    return prompts.update_prompt(payload.prompt)