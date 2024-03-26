from pydantic import BaseModel
from typing import List


class CharacterModel(BaseModel):
    char_name: str
    context: str

class CharactersModelList(BaseModel):
    characters: List[str]

class ResponsePostCharacterModel(BaseModel):
    message: str