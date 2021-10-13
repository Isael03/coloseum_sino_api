from models.modelssqlalchemy import especialidad
from config.db import database


class JobRepository:

    async def getJobId(self, job: str) -> int:
        query = especialidad.select(especialidad.c.id) \
            .where(especialidad.c.nombre_especialidad == job)
        res = await database.fetch_one(query=query)
        return res.id

    async def getJobs(self):
        query = especialidad.select()
        return await database.fetch_all(query=query)

