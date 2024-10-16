from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from core.settings import settings


class TipoSolicitacaoModel(settings.DBBaseModel):
    __tablename__ = 'tipo_solicitacao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(20))
