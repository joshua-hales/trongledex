from fastapi import FastAPI
from app.trongledex_api.app import router


app = FastAPI(
    title="Trongledex API",
)

app.include_router(router)
