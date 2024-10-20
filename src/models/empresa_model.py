from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import Mapped, mapped_column

from src.core.settings import settings


class EmpresaModel(settings.DBBaseModel):
    __tablename__ = 'empresa'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))
    cnpj: Mapped[str] = mapped_column(String(20))
    logo: Mapped[TEXT] = mapped_column(TEXT)
    url_evo: Mapped[str] = mapped_column(String(300))
    usuario_id: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(10))
    codigo_publico: Mapped[str] = mapped_column(String(10))
