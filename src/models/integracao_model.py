from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import BOOLEAN, TEXT, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from src.core.settings import settings


class IntegracaoModel(settings.DBBaseModel):
    __tablename__ = 'integracao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50))
    tipo_integracao_id: Mapped[int] = mapped_column(Integer)
    id_interno: Mapped[str] = mapped_column(String(200))
    usuario_id: Mapped[int] = mapped_column(Integer)
    empresa_id: Mapped[int] = mapped_column(Integer)
    conexao_id: Mapped[int] = mapped_column(Integer)
    setor_id: Mapped[int] = mapped_column(Integer)
