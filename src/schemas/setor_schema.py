from typing import Optional

from pydantic import BaseModel as PydanticBaseModel
from pydantic import field_validator


class SetorSchema(PydanticBaseModel):
    id: Optional[int] = None
    nome: str
    tipo: bool
    empresa_id: Optional[int] = None
    conexao_id: Optional[int] = None
    integracao_id: Optional[int] = None

    @field_validator('nome')
    def nome_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Nome é obrigatório.')

        return value
