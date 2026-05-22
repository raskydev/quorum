import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

#comunicação com banco de dados por meio de sessoes usando o sessionmaker e o engine.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#base para criar as tabelas do banco de dados.
Base = declarative_base()