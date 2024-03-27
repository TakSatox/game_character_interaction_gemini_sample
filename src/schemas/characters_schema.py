from pydantic import BaseModel


class CharactersSchema(BaseModel):
    character_name: str
    character_context: str