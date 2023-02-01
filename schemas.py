from pydantic import BaseModel

class Item(BaseModel):
    task:str
    rating:int

class Lead(BaseModel):
    id:int
    lead:str
