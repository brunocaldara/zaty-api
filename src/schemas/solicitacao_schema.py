from datetime import datetime
from typing import Optional

from pydantic import BaseModel as PydanticBaseModel
from pydantic import EmailStr, HttpUrl


class SolicitacaoSchema(PydanticBaseModel):
    id: Optional[int] = None
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    whatsapp: Optional[str] = None
    codigo_publico: Optional[str] = None
    validade: Optional[datetime]
    url: Optional[HttpUrl] = None
    status: Optional[str] = None
    tipo_solicitacao_id: Optional[int] = None
    usuario_id: Optional[int] = None
    nivel_usuario_id: Optional[int] = None
