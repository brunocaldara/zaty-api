from typing import Optional

from pydantic import BaseModel as PydanticBaseModel
from pydantic import field_validator


class UsuarioSchema(PydanticBaseModel):
    id: Optional[int] = None
    nome: str
    cpf: str
    email: str
    senha: str
    status: Optional[str] = None
    whatsapp: Optional[str] = None
    wizard: Optional[bool] = None
    empresa_id: Optional[int] = None
    nivel_usuario_id: Optional[int] = None
    setor_id: Optional[int] = None

    @field_validator('nome')
    def nome_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Nome é obrigatório.')

        return value

    @field_validator('cpf')
    def cpf_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo CPF é obrigatório.')

        return value

    @field_validator('email')
    def email_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo E-mail é obrigatório.')

        return value

    @field_validator('senha')
    def senha_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Senha é obrigatório.')

        return value
