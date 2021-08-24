import sqlalchemy
from .__init__ import metadata

gremio = sqlalchemy.Table(
    "Gremio",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("nombre", sqlalchemy.String),
)