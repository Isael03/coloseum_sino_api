from pydantic import BaseModel
from typing import Optional

class PlayerBase(BaseModel):
    id: Optional[int] = 0
    name: str = ""

class Player(PlayerBase):
    job: str = ""
    isMain: int = 0
    patk: int = 0
    matk: int = 0
    pdef: int = 0
    mdef: int = 0
    subJobs: Optional[list] = []



