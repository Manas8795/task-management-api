import os 

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

load_dotenv() # load the variable from the env where the postgres db connection link is there 

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL) # sql alchemy connection to postgresql

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False, #autoflush automatically flushes the pending data 
    bind = engine
)
Base = declarative_base() # this will give each fastAPi call ( request ) there separate session
# session is a temperary workspace or maybe a holding area type something 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# if __name__ == "__main__":
#     with engine.connect() as connection:
#         print("Database connection successful!")