from fastapi import APIRouter, status, HTTPException
from crud.interaction_spec import InteractionSpec
from models.interaction_model import InteractionModel


router = APIRouter()

# Get
@router.get("/{char_name}", status_code=status.HTTP_200_OK, response_model=InteractionModel)
async def get_character_response(char_name: str, question: str):
    interaction = InteractionSpec()
    formatted_prompt = interaction.format_prompt(char_name=char_name, question=question)

    if formatted_prompt:
        response = interaction.ask_gemini(formatted_prompt)
        return {"character_response": response}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found or the 'prompts' collection is empty")