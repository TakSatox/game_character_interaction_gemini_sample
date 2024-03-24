from pydantic import BaseModel


class InteractionModel(BaseModel):
    prompt: str
    response: str   