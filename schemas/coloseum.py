from pydantic import BaseModel
from typing import List, Dict

class Coloseum(BaseModel):
    members:List = None
    especs: List= None