from enum import Enum
from pydantic import BaseModel


class BandType(str, Enum):
    WHITE = "White"
    BLACK = "Black"
    BLACK_WHITE = "Black-white"
    BLACK_OTHER = "Black-other"


class Band(BaseModel):
    id:int 
    name:str
    type:BandType
    albums: list['Album'] = []


class Album(BaseModel):
    title:str
    release_date:str
    genre:str