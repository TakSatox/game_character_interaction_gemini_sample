from pydantic import BaseModel


class PromptModel(BaseModel):
    text: str
    last_change_timestamp: str