from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import BOOLEAN, TEXT, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from src.core.settings import settings


class SolicitacaoModel(settings.DBBaseModel):
    __tablename__ = 'pagina_conexao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(50))
    whatsapp: Mapped[str] = mapped_column(String(15))
    codigo_publico: Mapped[str] = mapped_column(String(10))
    validade: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    url: Mapped[str] = mapped_column(String(300))
    status: Mapped[str] = mapped_column(String(10))
    usuario_id: Mapped[int] = mapped_column(Integer)
    tipo_solicitacao_id: Mapped[int] = mapped_column(Integer)
    nivel_usuario_id: Mapped[int] = mapped_column(Integer)
