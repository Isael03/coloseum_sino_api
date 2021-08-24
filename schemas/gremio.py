from pydantic import BaseModel
from typing import Optional
from models.gremio import gremio
from config.db import database


class Gremio(BaseModel):
    id: Optional[int]
    nombre: str = None

    class Config:
        orm_mode = True

    def get_members(self):
        query = gremio.select()
        return database.fetch_all(query)
