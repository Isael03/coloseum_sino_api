from repositories.job_repository import JobRepository

class JobController:
    job = JobRepository()

    async def getAllJobs(self):
        jobs = [{"id": id, "name": name} for (id, name) in await self.job.getJobs()]
        return jobs

    async def onlyJobs(self):
        jobs = [name for (id, name) in await self.job.getJobs()]
        return jobs
