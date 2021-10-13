from fastapi import APIRouter
from controllers.job_controller import JobController
from schemas.job import JobBase

job = APIRouter()

jobController = JobController()


@job.get('/',
         response_model=list[JobBase],
         description='Obtener id y nombre de la especialidad'
         )
async def get_all_jobs():
    return await jobController.getAllJobs()


@job.get('/only_jobs',
         tags=["Jobs"], response_model=list[str],
         description='Obtener una lista de todas las especialidades'
         )
async def get_only_jobs():
    return await jobController.onlyJobs()
