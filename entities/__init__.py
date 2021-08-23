import sqlalchemy
from config.db import DATABASE_URL

metadata = sqlalchemy.MetaData()

try:
    engine = sqlalchemy.create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
    metadata.create_all(engine)
except Exception as e:
    print(e)