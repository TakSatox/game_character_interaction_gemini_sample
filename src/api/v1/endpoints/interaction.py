from fastapi import APIRouter, status, HTTPException
from crud.interaction_spec import InteractionSpec
from schemas.interaction_schema import InteractionSchema
from models.interaction_model import InteractionModel


router = APIRouter()

# Get
@router.post("/{char_name}", status_code=status.HTTP_200_OK, response_model=InteractionModel)
async def get_character_response(char_name: str, payload: InteractionSchema):
    interaction = InteractionSpec()
    formatted_prompt = interaction.format_prompt(char_name=char_name, question=payload.question)

    if formatted_prompt:
        response = interaction.ask_gemini(formatted_prompt)
        return {"character_response": response}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found or the 'prompts' collection is empty")