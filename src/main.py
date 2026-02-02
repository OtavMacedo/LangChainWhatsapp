from fastapi import FastAPI

from src.api.webhook import router

app = FastAPI()
app.include_router(router)
