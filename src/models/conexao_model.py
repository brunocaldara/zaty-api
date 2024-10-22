from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import BOOLEAN, TEXT, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from src.core.settings import settings


class ConexaoModel(settings.DBBaseModel):
    __tablename__ = 'conexao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50))
    nome_visual: Mapped[str] = mapped_column(String(50))
    token: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(10))
    tipo: Mapped[str] = mapped_column(String(15))
    whatsapp: Mapped[str] = mapped_column(String(15))
    id_interno: Mapped[str] = mapped_column(String(200))
    empresa_id: Mapped[int] = mapped_column(Integer)
    canal_id: Mapped[int] = mapped_column(Integer)
