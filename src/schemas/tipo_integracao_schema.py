from typing import Optional

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ValidationInfo, field_validator


class TipoIntegracaoSchema(PydanticBaseModel):
    id: Optional[int] = None
    logo: Optional[str] = None
    nome: str

    @field_validator('nome')
    def nome_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Nome é obrigatório.')

        return value
