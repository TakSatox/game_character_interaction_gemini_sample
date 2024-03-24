from pydantic import BaseModel
from typing import List


class CharacterModel(BaseModel):
    char_name: str
    char_context: str

class CharactersModelList(BaseModel):
    characters: List[str]