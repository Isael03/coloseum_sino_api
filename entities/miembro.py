import sqlalchemy
from .__init__ import metadata

miembro = sqlalchemy.Table(
    "Miembro",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("nombre", sqlalchemy.String),
)