import sqlalchemy
from config.db import metadata, engine
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table


gremio = sqlalchemy.Table(
    "Gremio",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("nombre", sqlalchemy.String),
)

jugador = sqlalchemy.Table(
    "Jugador",
    metadata,
    sqlalchemy.Column("jugador_id", Integer, primary_key=True,  autoincrement=True),
    sqlalchemy.Column("nombre", String, nullable=False),
)

especialidad = Table(
    "Especialidad",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nombre_especialidad", String(50)),
)

jugador_especialidad = Table(
    'Jugador_Especialidad',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('id_jugador', Integer, ForeignKey('Jugador.jugador_id',  onupdate="CASCADE", ondelete="CASCADE")),
    Column('id_especialidad', Integer, ForeignKey('Especialidad.id',  onupdate="CASCADE", ondelete="CASCADE")),
    Column('esPrincipal', Boolean),
    Column('patk', Integer, default=0),
    Column('matk', Integer, default=0),
    Column('pdef', Integer, default=0),
    Column('mdef', Integer, default=0)
)



metadata.create_all(engine)

