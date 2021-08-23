from fastapi import FastAPI
from config.db import database

from typing import Optional, List

#routes
from routes.coloseum_route import coloseum

#Models
from models.member import Member


app = FastAPI()

app.include_router(coloseum, prefix='/api/coloseum')

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get('/', response_model=List[Member])
async def index():
    members = Member()
    return await members.get_members()
