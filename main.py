from fastapi import FastAPI
import uvicorn
from config.db import database
from fastapi.middleware.cors import CORSMiddleware

# routes
from routes.guild_route import guild
from routes.job_route import job


def create_app() -> FastAPI:

    app = FastAPI(title='GuildSinoalice', description='Gestionar gremio de sinoalice')

    origins = [
        "http://localhost:3000",
    ]

    app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    # Add_routes
    app.include_router(guild, prefix='/api/player', tags=['Player'])
    app.include_router(job, prefix='/api/job', tags=['Jobs'])

    @app.get('/')
    async def index():
        return 'Hi'

    return app


app = create_app()

#Debugging
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

