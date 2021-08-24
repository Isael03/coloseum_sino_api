from fastapi import FastAPI
from config.db import database
from typing import Optional, List


#routes
from routes.coloseum_route import coloseum

#Models
from schemas.member import Member


def create_app() -> FastAPI:

    app = FastAPI()
    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    # Add_routes
    app.include_router(coloseum, prefix='/api/coloseum')

    @app.get('/', response_model=List[Member])
    async def index():
        return 'Hi'

    return app

app = create_app()