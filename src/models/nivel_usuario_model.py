from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.settings import settings


class NivelUsuarioModel(settings.DBBaseModel):
    __tablename__ = 'nivel_usuario'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(20))
