from sqlalchemy import Boolean, Integer, String
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import Mapped, mapped_column

from src.core.settings import settings


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuario'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))
    cpf: Mapped[str] = mapped_column(String(15))
    email: Mapped[str] = mapped_column(String(50))
    senha: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(10))
    whatsapp: Mapped[str] = mapped_column(String(15))
    wizard: Mapped[bool] = mapped_column(Boolean)
    empresa_id: Mapped[int] = mapped_column(Integer)
    nivel_usuario_id: Mapped[int] = mapped_column(Integer)
    setor_id: Mapped[int] = mapped_column(Integer)
