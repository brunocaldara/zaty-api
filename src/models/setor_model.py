from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.settings import settings


class SetorModel(settings.DBBaseModel):
    __tablename__ = 'setor'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50))
    tipo: Mapped[bool] = mapped_column(Boolean)
    empresa_id: Mapped[int] = mapped_column(Integer)
    conexao_id: Mapped[int] = mapped_column(Integer)
    integracao_id: Mapped[int] = mapped_column(Integer)
