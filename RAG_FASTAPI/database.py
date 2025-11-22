from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Field, Session, select, create_engine
from typing import Optional, List

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url)


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = None
    
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    
    salary: Optional[float] = None


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


app = FastAPI(on_startup=[create_db_and_tables])