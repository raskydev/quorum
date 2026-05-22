from app.core.database import Base
from sqlalchemy import Column, Integer, String

class Funcionario(Base):
    __tablename__ = "funcionarios"
    id =  Column (Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    cargo = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    nivel_acesso = Column(Integer, nullable=False)
    setor = Column(String, nullable=False)
