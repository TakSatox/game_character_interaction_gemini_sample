from pydantic import BaseModel


class InteractionSchema(BaseModel):
    question: str