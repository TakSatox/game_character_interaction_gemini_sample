from fastapi import FastAPI
from models.healthcheck_model import HealthCheckModel
from api.v1.api import api_router


app = FastAPI(title="Character Interaction with Gemini")

# Health check
@app.get("/", response_model=HealthCheckModel, tags=["HealthCheck"])
async def health_check():
    return {"message": "OK"}

# Include endpoints
app.include_router(api_router, prefix="/api/v1")