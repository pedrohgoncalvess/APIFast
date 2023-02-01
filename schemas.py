from pydantic import BaseModel
from typing import List, Dict

class Item(BaseModel):
    task:str
    rating:int

class Lead(BaseModel):
    id:int
    lead_name:str
    lead:str

