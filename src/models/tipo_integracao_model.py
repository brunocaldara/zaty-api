from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import Mapped, mapped_column

from src.core.settings import settings


class TipoIntegracaoModel(settings.DBBaseModel):
    __tablename__ = 'tipo_integracao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    logo: Mapped[TEXT] = mapped_column(TEXT)
    nome: Mapped[str] = mapped_column(String(20))
