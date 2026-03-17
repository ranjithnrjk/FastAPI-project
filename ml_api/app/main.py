from fastapi import FastAPI
from ml_api.app.api.routes.health import router as health_router

app = FastAPI()

app.include_router(health_router)