from datetime import datetime
from typing import Optional

from pydantic import BaseModel as PydanticBaseModel


class AtendimentoSchema(PydanticBaseModel):
    id: Optional[int] = None
    id_interno: Optional[str] = None
    numero: Optional[str] = None
    tipo_mensagem: Optional[str] = None
    nome: Optional[str] = None
    mensagem: Optional[str] = None
    foto_perfil: Optional[str] = None
    data_hora: Optional[datetime]
    dispositivo: Optional[str] = None
    enviada_por_mim: Optional[bool]
    tipo_atendimento: Optional[str] = None
    primeiro_registro: Optional[datetime]
    ultimo_registro: Optional[datetime]
    status: Optional[str] = None
    empresa_id: Optional[int] = None
    usuario_id: Optional[int] = None
    conexao_id: Optional[int] = None
    setor_id: Optional[int] = None
    canal_id: Optional[int] = None
