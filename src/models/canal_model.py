from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.settings import settings


class CanalModel(settings.DBBaseModel):
    __tablename__ = 'canal'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(20))
