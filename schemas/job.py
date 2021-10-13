from pydantic import BaseModel
from typing import Optional


class JobBase(BaseModel):
    id: Optional[int] = 0
    name: str = ""
