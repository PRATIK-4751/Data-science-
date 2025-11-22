# we will do pydantic libraries ! 
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
 