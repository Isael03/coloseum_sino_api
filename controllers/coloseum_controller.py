from schemas.member import Member
from schemas.coloseum import Coloseum
from models.miembro import miembro
from config.db import database

class ColoseumController(Coloseum):

    async def getAllMembersAndSpecs(self):
        query = miembro.select()
        return await database.fetch_all(query)