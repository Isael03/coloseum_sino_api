from pydantic import BaseModel
from typing import Optional
#from models.miembro import miembro
from config.db import database


class Member(BaseModel):
    miembro_id: Optional[int]
    nombre: str = None

    class Config:
        orm_mode = True


    def get_members(self):
        # query = miembro.select()
        # return database.fetch_all(query)
        pass

