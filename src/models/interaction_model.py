from pydantic import BaseModel


class InteractionModel(BaseModel):
    character_response: str   