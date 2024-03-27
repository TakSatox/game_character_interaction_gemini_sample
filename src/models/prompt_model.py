from pydantic import BaseModel
from datetime import date


class PromptModel(BaseModel):
    prompt: str
    created_at: date

class ResponseUpdatePromptModel(BaseModel):
    message: str