import sqlalchemy
from config.db import metadata, engine
from models.especialidad import miembro_especialidad
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


miembro = sqlalchemy.Table(
    "Miembro",
    metadata,
    sqlalchemy.Column("miembro_id", sqlalchemy.Integer, primary_key=True,  autoincrement=True),
    sqlalchemy.Column("nombre", sqlalchemy.String, nullable=False),
    #relationship("Especialidad", secondary=miembro_especialidad)
)

metadata.create_all(engine)

