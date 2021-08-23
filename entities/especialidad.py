import sqlalchemy
from .__init__ import metadata

especialidad = sqlalchemy.Table(
    "Especialidad",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("nombre", sqlalchemy.String),
)