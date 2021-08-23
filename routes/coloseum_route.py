from fastapi import APIRouter

coloseum = APIRouter()

@coloseum.get('/', tags=["coloseum"])
def get_planner():
    return 'Coliseo'