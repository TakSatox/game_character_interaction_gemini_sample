from fastapi import APIRouter, status, HTTPException
from crud.interaction_spec import InteractionSpec
from schemas.interaction_schema import InteractionSchema
from models.interaction_model import InteractionModel


router = APIRouter()

# Get
@router.post("/{char_name}", status_code=status.HTTP_200_OK, response_model=InteractionModel)
async def get_character_response(char_name: str, payload: InteractionSchema):
    pass