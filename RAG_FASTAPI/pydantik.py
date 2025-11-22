# we will do pydantic libraries ! 
from enum import Enum
from pydantic import BaseModel
from typing import Optional
from datetime import date



class BandType(str, Enum):
    WHITE = "White"
    BLACK = "Black"
    BLACK_WHITE = "Black-white"
    BLACK_OTHER = "Black-other"



class Album(BaseModel):
    title : str 
    release_date: date 


class Band(BaseModel):
    id:int 
    name:str
    type: Optional[BandType] = None
    albums : Optional[list[Album]] = None
 