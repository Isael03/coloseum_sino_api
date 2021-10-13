from schemas.player import Player
from repositories.player_repository import PlayerRepository
from repositories.job_repository import JobRepository


class PlayerController():
    player = PlayerRepository()
    job = JobRepository()
    playerSchema = Player()

    def getAllMembersAndSpecs(self) -> list():
        return self.player.getAllMembersAndSpecs()

    def getPLayer(self, id: playerSchema.id):
        return self.player.getPlayer(id)

    def deletePlayer(self, id: playerSchema.id):
        return self.player.deletePlayer(id)

    async def createPlayer(self, player: dict):
        job_id: int = await self.job.getJobId(player.job)
        player_id: int = await self.player.createPlayer(player=player, id_job=job_id)

        for job in player.subJobs:
            job_id = await self.job.getJobId(job)
            await self.player.addPlayerJob(id_player=player_id, id_job=job_id, player=player, isMain=False)

    async def getAllJobs(self):
        jobs = await self.job.getJobs()
