from fastapi import FastAPI
from schemas.healthcheck import HealthCheck
from api.v1.api import api_router

app = FastAPI(title="Character Interaction with Gemini")


@app.get("/", response_model=HealthCheck, tags=["HealthCheck"])
async def health_check():
    return {"message": "OK"}

app.include_router(api_router, prefix="/api/v1")