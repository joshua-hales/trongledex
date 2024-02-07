from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select

from trongledex_api.database import create_db_and_tables, engine
from trongledex_api.models import Trongle

app = FastAPI()


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()


@app.get("/trongles/")
async def read_trongles() -> list[Trongle]:
    """Returns all trongles from the database."""
    with Session(engine) as session:
        trongles = session.exec(select(Trongle)).all()
        return trongles


@app.post("/trongles/")
async def create_trongle(trongle: Trongle) -> Trongle:
    """Creates a new trongle in the database."""
    with Session(engine) as session:
        session.add(trongle)
        session.commit()
        session.refresh(trongle)
        return trongle


@app.get("/trongles/{trongle_id}")
async def read_trongle(trongle_id: int) -> Trongle:
    """Returns the matching trongle from the database."""
    with Session(engine) as session:
        trongle = session.get(Trongle, trongle_id)
        if not trongle:
            raise HTTPException(status_code=404, detail="trongle not found")
        return trongle
