from typing import Optional

from pydantic import BaseModel as PydanticBaseModel
from pydantic import field_validator


class IntegracaoSchema(PydanticBaseModel):
    id: Optional[int] = None
    nome: str
    id_interno: Optional[str] = None
    tipo_integracao_id: Optional[int] = None
    usuario_id: Optional[int] = None
    empresa_id: Optional[int] = None
    conexao_id: Optional[int] = None
    setor_id: Optional[int] = None

    @field_validator('nome')
    def nome_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Nome é obrigatório.')

        return value
