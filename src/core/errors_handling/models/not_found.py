from pydantic import BaseModel


class NotFoundModel(BaseModel):
    detail: str