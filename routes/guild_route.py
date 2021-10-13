from fastapi import APIRouter, Response, status
from controllers.player_controller import PlayerController
from schemas.player import Player

from config.db import database
from repositories.player_repository import PlayerRepository
from models.modelssqlalchemy import jugador, especialidad, jugador_especialidad

guild = APIRouter()
playerSchema = Player()


@guild.get('/', tags=["Player"], response_model=list[Player], description='Mostrar a todos los jugadores')
async def get_players():
    return await PlayerController().getAllMembersAndSpecs()


@guild.get('/{id}', response_model=Player, description='Obtener un jugador específico')
async def get_player(id: int):
    return await PlayerController().getPLayer(id)


@guild.delete('/{id}', description='Borrar a jugador')
async def delete_player(id: int):
    await PlayerController().deletePlayer(id)
    return status.HTTP_204_NO_CONTENT


@guild.post('/', status_code=status.HTTP_201_CREATED, description='Ingresar nuevo jugador al gremio')
async def add_player(player: Player):
    try:
        await PlayerController().createPlayer(player)
        return status.HTTP_201_CREATED
    except Exception:
        return status.HTTP_409_CONFLICT
