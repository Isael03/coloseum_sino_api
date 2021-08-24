import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from config.db import metadata, engine


miembro_especialidad = Table(
    'Miembro_Especialidad',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('miembro', Integer, ForeignKey('Miembro.miembro_id')),
    Column('especialidad', Integer, ForeignKey('Especialidad.id')),
    #relationship('especialidad', back_populates="parents"),
    #relationship('Miembro', back_populates="children")
)

especialidad = Table(
    "Especialidad",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nombre", String),
    #relationship("Miembro", secondary=miembro_especialidad, back_populates="children")
)
# miembro = sqlalchemy.Table(
#     "Miembro",
#     metadata,
#     sqlalchemy.Column("miembro_id", sqlalchemy.Integer, primary_key=True,  autoincrement=True),
#     sqlalchemy.Column("nombre", sqlalchemy.String, nullable=False),
#     #relationship("Especialidad", secondary=miembro_especialidad)
# )

metadata.create_all(engine)
