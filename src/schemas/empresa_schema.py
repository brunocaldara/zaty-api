from typing import Optional

from pydantic import BaseModel as PydanticBaseModel
from pydantic import HttpUrl, field_validator


class EmpresaSchema(PydanticBaseModel):
    id: Optional[int] = None
    nome: str
    cnpj: str
    logo: Optional[str] = None
    url_evo: Optional[HttpUrl] = None
    usuario_id: Optional[int] = None
    status: Optional[str] = None
    codigo_publico: Optional[str] = None

    @field_validator('nome')
    def nome_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Nome é obrigatório.')

        return value

    @field_validator('cnpj')
    def cnpj_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo CNPJ é obrigatório.')

        return value
