import datetime

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str


class Emotion(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str


class Trongle(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str = ""
    emotion: int | None = Field(default=None, foreign_key="emotion.id")
    image_url: str | None = None
    edges: int = 3
    faces: int = 1
    vertices: int = 3
    created_on: datetime.date | None = None
    created_by: int | None = Field(default=None, foreign_key="user.id")
