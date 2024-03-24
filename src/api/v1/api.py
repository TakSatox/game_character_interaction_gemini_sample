from fastapi import APIRouter
from api.v1.endpoints import interaction, prompt, characters


api_router = APIRouter()

api_router.include_router(interaction.router, prefix="/interaction", tags=["Interaction"])
api_router.include_router(prompt.router, prefix="/prompt", tags=["Prompt"])
api_router.include_router(characters.router, prefix="/characters", tags=["Characters"])
