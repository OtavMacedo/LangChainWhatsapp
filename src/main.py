from dotenv import load_dotenv

from fastapi import FastAPI

from src.api.webhook import router

load_dotenv()


app = FastAPI(title="Agent João - Personal Trainer Qualifier")
app.include_router(router)
