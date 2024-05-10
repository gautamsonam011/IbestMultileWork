from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative  import declarative_base

DATABASE_URL = 'postgresql://postgres:Sonam%40123@localhost:5432/postgres'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, bind =engine)
Base = declarative_base()

