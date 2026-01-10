from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from contrib.models import BaseModel


class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centro_treinamento'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)

    atleta: Mapped[List["AtletaModel"]] = relationship("AtletaModel", back_populates="centro_treinamento")