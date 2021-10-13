from models.modelssqlalchemy import jugador, jugador_especialidad, especialidad
from schemas.player import Player
from config.db import database

playerSchema = Player()


class PlayerRepository:
    id: int = 0
    nombre: str = ""
    id_especialidad: int = 0
    job: str = ""
    esPrincipal: int = 0
    patk: int = 0
    matk: int = 0
    pdef: int = 0
    mdef: int = 0
    subJobs: list = []

    def __init__(self, id: int = 0, name: str = "", job: str = "", isMain: int = 0, patk: int = 0, matk: int = 0,
                 pdef: int = 0,
                 mdef: int = 0,
                 subJobs: list = []):
        self.id = id
        self.name = name
        self.job = job
        self.isMain = isMain
        self.patk = patk
        self.matk = matk
        self.pdef = pdef
        self.mdef = mdef
        self.subJobs = subJobs

    def getAllMembersAndSpecs(self) -> list[Player]:
        try:
            query = """select J.jugador_id as id, J.nombre as name, E.nombre_especialidad as job, JE.esPrincipal as isMain, JE.patk, JE.matk, JE.pdef, JE.mdef from Jugador J
            inner join Jugador_Especialidad JE on J.jugador_id = JE.id_jugador
            inner join Especialidad E on E.id = JE.id_especialidad"""
            return database.fetch_all(query=query)
        except Exception as e:
            return print(e)

    async def deletePlayer(self, id: playerSchema.id):
        try:
            query = jugador_especialidad.delete().where(jugador_especialidad.c.id_jugador == id)
            await database.execute(query)
            query = 'DELETE FROM Jugador Where jugador_id = :id'
            await database.execute(query=query, values={"id": id})
        except Exception as e:
            print(e)

    async def getPlayer(self, id: playerSchema.id) -> Player:
        print(id)
        try:
            query = """select J.jugador_id as id, J.nombre as name, E.nombre_especialidad as job, 
            JE.esPrincipal as isMainJob, JE.patk, JE.matk, JE.pdef, JE.mdef from Jugador J
            inner join Jugador_Especialidad JE on J.jugador_id = JE.id_jugador
            inner join Especialidad E on E.id = JE.id_especialidad WHERE J.jugador_id = {id}""".format(id=id)
            return await database.fetch_one(query=query)

        except Exception as e:
            print(e)

    def updatePlayer(self):
        pass

    async def createPlayer(self, player: dict, id_job: int):
        try:
            # Comprobar si el jugador existe
            query = 'SELECT jugador_id FROM Jugador WHERE nombre = :nombre'
            res = await database.fetch_one(query=query, values={"nombre": player.name})

            # Si el jugador existe devolver
            if (res != None):
                return

            # Registrar jugador
            query = jugador.insert()
            id_player: int = await database.execute(query=query, values={"nombre": player.name})

            # Registrar job principal en la tabla jugador_especialidad
            await self.addPlayerJob(id_player=id_player, id_job=id_job, player=player, isMain=True)

            return id_player
        except Exception as e:
            print(e)

    async def addPlayerJob(self, id_player, id_job, player, isMain: bool = True):
        try:
            query = jugador_especialidad.insert()
            new_playerEspec = {
                "id_jugador": id_player,
                "id_especialidad": id_job,
                "esPrincipal": player.isMain,
                "patk": player.patk,
                "matk": player.matk,
                "pdef": player.pdef,
                "mdef": player.mdef
            }
            if isMain == False:
                new_playerEspec['esPrincipal'] = 0

            await database.execute(query=query, values=new_playerEspec)
        except Exception as e:
            print(e)
