from fastapi import APIRouter, status, HTTPException
from schemas.interaction_schema import InteractionSchema
from models.interaction_model import InteractionModel


router = APIRouter()

# Get
@router.post("/{char_id}", status_code=status.HTTP_200_OK, response_model=InteractionModel)
async def get_character_response(char_id: str, payload: InteractionSchema):
    pass
    # return sample: {"prompt": "voce é um chatbot, pergunta do usuario: a, contexto do char: b", "response": "eu sou eva, a pioneira das construções napoleônicas!"}