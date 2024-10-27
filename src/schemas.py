from datetime import datetime
from typing import Optional

from pydantic import BaseModel as PydanticBaseModel
from pydantic import EmailStr, HttpUrl, field_validator


class CanalSchema(PydanticBaseModel):
    id: Optional[int] = None
    nome: str

    @field_validator('nome')
    def nome_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Nome é obrigatório.')

        return value


class NivelUsuarioSchema(PydanticBaseModel):
    id: Optional[int] = None
    nome: str

    @field_validator('nome')
    def nome_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Nome é obrigatório.')

        return value


class TipoIntegracaoSchema(PydanticBaseModel):
    id: Optional[int] = None
    logo: Optional[str] = None
    nome: str

    @field_validator('nome')
    def nome_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Nome é obrigatório.')

        return value


class TipoSolicitacaoSchema(PydanticBaseModel):
    id: Optional[int] = None
    nome: str

    @field_validator('nome')
    def nome_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Nome é obrigatório.')

        return value


class EmpresaSchemaBase(PydanticBaseModel):
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


class ConexaoSchemaBase(PydanticBaseModel):
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


class ConexaoSchema(ConexaoSchemaBase):
    empresa: Optional[EmpresaSchemaBase] = None
    canal: Optional[CanalSchema] = None


class UsuarioSchemaBase(PydanticBaseModel):
    id: Optional[int] = None
    nome: str
    cpf: str
    email: EmailStr
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


class IntegracaoSchemaBase(PydanticBaseModel):
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


class SetorSchemaBase(PydanticBaseModel):
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


class AtendimentoSchemaBase(PydanticBaseModel):
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


class AtendimentoSchema(AtendimentoSchemaBase):
    empresa: Optional[EmpresaSchemaBase] = None
    usuario: Optional[UsuarioSchemaBase] = None
    conexao: Optional[ConexaoSchemaBase] = None
    setor: Optional[SetorSchemaBase] = None
    canal: Optional[CanalSchema] = None


class EmpresaSchema(EmpresaSchemaBase):
    usuario: Optional[UsuarioSchemaBase] = None


class IntegracaoSchema(PydanticBaseModel):
    tipo_integracao: Optional[TipoIntegracaoSchema] = None
    usuario: Optional[UsuarioSchemaBase] = None
    empresa: Optional[EmpresaSchemaBase] = None
    conexao: Optional[ConexaoSchemaBase] = None
    setor: Optional[SetorSchemaBase] = None


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
    empresa: Optional[EmpresaSchemaBase] = None
    usuario: Optional[UsuarioSchemaBase] = None
    conexao: Optional[ConexaoSchemaBase] = None


class SetorSchema(SetorSchemaBase):
    empresa: Optional[EmpresaSchemaBase] = None
    conexao: Optional[ConexaoSchemaBase] = None
    integracao: Optional[IntegracaoSchemaBase] = None


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
    tipo_solicitacao: Optional[TipoIntegracaoSchema] = None
    usuario: Optional[UsuarioSchemaBase] = None
    nivel_usuario: Optional[NivelUsuarioSchema] = None


class UsuarioSchema(UsuarioSchemaBase):
    empresa: Optional[EmpresaSchema] = None
    nivel_usuario: Optional[NivelUsuarioSchema] = None
    setor: Optional[SetorSchemaBase] = None


class UsuarioSchemaCreate(UsuarioSchema):
    senha: str

    @field_validator('senha')
    def senha_validator(cls, value: str):
        if value is None or value.strip() == '':
            raise ValueError('Campo Senha é obrigatório.')

        return value


class UsuarioSchemaChangePassword(PydanticBaseModel):
    email: EmailStr
    senha_atual: str
    senha_nova: str
