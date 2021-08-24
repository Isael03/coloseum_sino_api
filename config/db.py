import databases
import sqlalchemy

try:
    DATABASE_URL = 'sqlite:///db.s3db'
    database = databases.Database(DATABASE_URL)
    metadata = sqlalchemy.MetaData()
    engine = sqlalchemy.create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
    #metadata.create_all(engine)
except Exception as e:
    print(e)
