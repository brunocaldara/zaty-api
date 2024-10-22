from typing import Optional

from pydantic import BaseModel as PydanticBaseModel


class PaginaConexaoSchema(PydanticBaseModel):
    id: Optional[int] = None
    token: Optional[str] = None
    status: Optional[str] = None
    hash_url: Optional[str] = None
    protegida: Optional[bool] = None
    senha_protecao: Optional[str] = None
    empresa_id: Optional[int] = None
    usuario_id: Optional[int] = None
    conexao_id: Optional[int] = None
