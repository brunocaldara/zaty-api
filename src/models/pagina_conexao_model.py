from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import BOOLEAN, TEXT, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from src.core.settings import settings


class PaginaConexaoModel(settings.DBBaseModel):
    __tablename__ = 'pagina_conexao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    token: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(10))
    hash_url: Mapped[str] = mapped_column(String(500))
    protegida: Mapped[BOOLEAN] = mapped_column(BOOLEAN)
    senha_protecao: Mapped[str] = mapped_column(String(255))
    usuario_id: Mapped[int] = mapped_column(Integer)
    empresa_id: Mapped[int] = mapped_column(Integer)
    conexao_id: Mapped[int] = mapped_column(Integer)
