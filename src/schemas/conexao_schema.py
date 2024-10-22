from typing import Optional

from pydantic import BaseModel as PydanticBaseModel
from pydantic import field_validator


class ConexaoSchema(PydanticBaseModel):
    id: Optional[int] = None
    nome: str
    nome_visual: str
    token: str
    status: Optional[str] = None
    empresa_id: Optional[int] = None
    tipo: Optional[str] = None
    whatsapp: Optional[str] = None
    id_interno: Optional[str] = None
    canal_id: Optional[int] = None

    @field_validator('nome')
    def nome_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Nome é obrigatório.')

        return value

    @field_validator('nome_visual')
    def nome_visual_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Nome Visual é obrigatório.')

        return value

    @field_validator('token')
    def token_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Token é obrigatório.')

        return value
