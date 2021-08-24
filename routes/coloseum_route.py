from fastapi import APIRouter, Response
from controllers.coloseum_controller import ColoseumController
from schemas.member import Member
from typing import List

coloseum = APIRouter()

@coloseum.get('/', tags=["Coloseum"], response_model=List[Member])
async def get_planner( response= Response):
    data = await ColoseumController().getAllMembersAndSpecs()
    response.status_code = 200
    return data


    #return 'Coliseo'