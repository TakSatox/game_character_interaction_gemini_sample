from fastapi import APIRouter, status, HTTPException
from crud.characters_spec import CharactersSpec
from schemas.characters_schema import CharactersSchema
from models.characters_model import CharacterModel, CharactersModelList, ResponsePostCharacterModel
from core.errors_handling.models.not_found import NotFoundModel


# Router Decorator
router = APIRouter()

# Get
@router.get("/{char_name}", status_code=status.HTTP_200_OK, response_model=CharacterModel, responses={
    status.HTTP_404_NOT_FOUND: {
        "model": NotFoundModel
    }
})
async def get_character_info(char_name: str):
    characters= CharactersSpec()
    character_info = characters.get_character_info(char_name)
    if character_info:
        return character_info
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found")

# List
@router.get("", status_code=status.HTTP_200_OK, response_model=CharactersModelList)
@router.get("/", status_code=status.HTTP_200_OK, include_in_schema=False, response_model=CharactersModelList, responses={
    status.HTTP_404_NOT_FOUND: {
        "model": NotFoundModel
    }
})
async def list_characters_names():
    characters = CharactersSpec()
    characters_name = characters.list_characters_name()   
    if characters_name:
        return {"characters": characters_name}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The 'characters' collection is empty or does not exist")

# Post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ResponsePostCharacterModel)
async def add_new_character(payload: CharactersSchema):
    characters = CharactersSpec()
    return characters.add_character(char_name=payload.character_name, char_context=payload.character_context)

