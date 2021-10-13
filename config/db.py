from sqlalchemy import create_engine, MetaData
import databases
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///db.s3db"
database = databases.Database(DATABASE_URL)

metadata = MetaData()

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata.create_all(engine)


