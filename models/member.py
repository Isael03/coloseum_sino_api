from pydantic import BaseModel
from typing import Optional
from entities.miembro import miembro
from config.db import database


class Member(BaseModel):
    id: Optional[int]
    nombre: str = None

    def get_members(self):
        query = miembro.select()
        return database.fetch_all(query)
