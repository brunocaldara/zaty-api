from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import Mapped, mapped_column

from src.core.settings import settings


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuario'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))
