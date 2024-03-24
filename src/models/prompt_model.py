from pydantic import BaseModel

class PromptModel(BaseModel):
    text: str
    created_at: str