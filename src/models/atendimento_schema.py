from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import BOOLEAN, TEXT, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from src.core.settings import settings


class AtendimentoModel(settings.DBBaseModel):
    __tablename__ = 'atendimento'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_interno: Mapped[str] = mapped_column(String(200))
    numero: Mapped[str] = mapped_column(String(200))
    nome: Mapped[str] = mapped_column(String(50))
    tipo_mensagem: Mapped[str] = mapped_column(String(20))
    mensagem: Mapped[str] = mapped_column(String(100))
    foto_perfil: Mapped[TEXT] = mapped_column(TEXT)
    data_hora: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    dispositivo: Mapped[str] = mapped_column(String(10))
    enviada_por_mim: Mapped[BOOLEAN] = mapped_column(BOOLEAN)
    tipo_atendimento: Mapped[str] = mapped_column(String(10))
    primeiro_registro: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    ultimo_registro: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    status: Mapped[str] = mapped_column(String(10))
    empresa_id: Mapped[int] = mapped_column(Integer)
    usuario_id: Mapped[int] = mapped_column(Integer)
    conexao_id: Mapped[int] = mapped_column(Integer)
    setor_id: Mapped[int] = mapped_column(Integer)
    canal_id: Mapped[int] = mapped_column(Integer)
