from fastapi import APIRouter, status, HTTPException
from models.characters_model import CharacterModel, CharactersModelList


router = APIRouter()


# Get
@router.get("/{char_name}", status_code=status.HTTP_200_OK, response_model=CharacterModel)
async def get_character_info(char_name: str):
    pass
    # return sample: return {"char_name": char_name, "char_context": f"nascido em 1990, o char {char_name} avaliou todos os continentes"}

# List
@router.get("/", status_code=status.HTTP_200_OK, response_model=CharactersModelList)
async def list_characters_info():
    pass
    # return sample: {"characters": ["brendon", "calavo", "frank", "manobrown"]}
