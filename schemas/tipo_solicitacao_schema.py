from typing import Optional

from pydantic import BaseModel as PydanticBaseModel


class TipoSolicitacaoSchema(PydanticBaseModel):
    id: Optional[int] = None
    nome: str

    # class Config:
    #     orm_mode = True
