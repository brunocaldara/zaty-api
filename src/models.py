from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import BOOLEAN, TEXT, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.settings import settings


class AtendimentoModel(settings.DBBaseModel):
    __tablename__ = 'atendimento'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_interno: Mapped[str] = mapped_column(String(200))
    numero: Mapped[str] = mapped_column(String(200))
    nome: Mapped[str] = mapped_column(String(50))
    tipo_mensagem: Mapped[str] = mapped_column(String(20))
    mensagem: Mapped[str] = mapped_column(String(100))
    foto_perfil: Mapped[TEXT] = mapped_column(TEXT)
    data_hora: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    dispositivo: Mapped[str] = mapped_column(String(10))
    enviada_por_mim: Mapped[BOOLEAN] = mapped_column(BOOLEAN)
    tipo_atendimento: Mapped[str] = mapped_column(String(10))
    primeiro_registro: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    ultimo_registro: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    status: Mapped[str] = mapped_column(String(10))
    empresa_id: Mapped[int] = mapped_column(ForeignKey('empresa.id'))
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'))
    conexao_id: Mapped[int] = mapped_column(ForeignKey('conexao.id'))
    setor_id: Mapped[int] = mapped_column(ForeignKey('setor.id'))
    canal_id: Mapped[int] = mapped_column(ForeignKey('canal.id'))
    empresa: Mapped['EmpresaModel'] = relationship(lazy='joined')
    usuario: Mapped['UsuarioModel'] = relationship(lazy='joined')
    conexao: Mapped['ConexaoModel'] = relationship(lazy='joined')
    setor: Mapped['SetorModel'] = relationship(lazy='joined')
    canal: Mapped['CanalModel'] = relationship(lazy='joined')


class CanalModel(settings.DBBaseModel):
    __tablename__ = 'canal'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(20))


class ConexaoModel(settings.DBBaseModel):
    __tablename__ = 'conexao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50))
    nome_visual: Mapped[str] = mapped_column(String(50))
    token: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(10))
    tipo: Mapped[str] = mapped_column(String(15))
    whatsapp: Mapped[str] = mapped_column(String(15))
    id_interno: Mapped[str] = mapped_column(String(200))
    empresa_id: Mapped[int] = mapped_column(ForeignKey('empresa.id'))
    canal_id: Mapped[int] = mapped_column(ForeignKey('canal.id'))
    empresa: Mapped['EmpresaModel'] = relationship(lazy='joined')
    canal: Mapped['CanalModel'] = relationship(lazy='joined')


class EmpresaModel(settings.DBBaseModel):
    __tablename__ = 'empresa'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))
    cnpj: Mapped[str] = mapped_column(String(20))
    logo: Mapped[TEXT] = mapped_column(TEXT)
    url_evo: Mapped[str] = mapped_column(String(300))
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'))
    status: Mapped[str] = mapped_column(String(10))
    codigo_publico: Mapped[str] = mapped_column(String(10))
    usuario: Mapped['UsuarioModel'] = relationship(
        lazy='joined', foreign_keys=[usuario_id])


class IntegracaoModel(settings.DBBaseModel):
    __tablename__ = 'integracao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50))
    tipo_integracao_id: Mapped[int] = mapped_column(Integer)
    id_interno: Mapped[str] = mapped_column(String(200))
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'))
    empresa_id: Mapped[int] = mapped_column(ForeignKey('empresa.id'))
    conexao_id: Mapped[int] = mapped_column(ForeignKey('conexao.id'))
    setor_id: Mapped[int] = mapped_column(ForeignKey('setor.id'))
    usuario: Mapped['UsuarioModel'] = relationship(
        lazy='joined', foreign_keys=[usuario_id])
    empresa: Mapped['EmpresaModel'] = relationship(
        lazy='joined', foreign_keys=[empresa_id])
    conexao: Mapped['ConexaoModel'] = relationship(
        lazy='joined', foreign_keys=[conexao_id])
    setor: Mapped['SetorModel'] = relationship(
        lazy='joined', foreign_keys=[setor_id])


class NivelUsuarioModel(settings.DBBaseModel):
    __tablename__ = 'nivel_usuario'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(20))


class PaginaConexaoModel(settings.DBBaseModel):
    __tablename__ = 'pagina_conexao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    token: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(10))
    hash_url: Mapped[str] = mapped_column(String(500))
    protegida: Mapped[BOOLEAN] = mapped_column(BOOLEAN)
    senha_protecao: Mapped[str] = mapped_column(String(255))
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'))
    empresa_id: Mapped[int] = mapped_column(ForeignKey('empresa.id'))
    conexao_id: Mapped[int] = mapped_column(ForeignKey('conexao.id'))
    usuario: Mapped['UsuarioModel'] = relationship(
        lazy='joined', foreign_keys=[usuario_id])
    empresa: Mapped['EmpresaModel'] = relationship(
        lazy='joined', foreign_keys=[empresa_id])
    conexao: Mapped['ConexaoModel'] = relationship(
        lazy='joined', foreign_keys=[conexao_id])


class SetorModel(settings.DBBaseModel):
    __tablename__ = 'setor'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50))
    tipo: Mapped[bool] = mapped_column(Boolean)
    empresa_id: Mapped[int] = mapped_column(ForeignKey('empresa.id'))
    conexao_id: Mapped[int] = mapped_column(ForeignKey('conexao.id'))
    integracao_id: Mapped[int] = mapped_column(ForeignKey('integracao.id'))
    empresa: Mapped['EmpresaModel'] = relationship(
        lazy='joined', foreign_keys=[empresa_id])
    conexao: Mapped['ConexaoModel'] = relationship(
        lazy='joined', foreign_keys=[conexao_id])
    integracao: Mapped['IntegracaoModel'] = relationship(
        lazy='joined', foreign_keys=[integracao_id])


class SolicitacaoModel(settings.DBBaseModel):
    __tablename__ = 'solicitacao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(50))
    whatsapp: Mapped[str] = mapped_column(String(15))
    codigo_publico: Mapped[str] = mapped_column(String(10))
    validade: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    url: Mapped[str] = mapped_column(String(300))
    status: Mapped[str] = mapped_column(String(10))
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'))
    tipo_solicitacao_id: Mapped[int] = mapped_column(
        ForeignKey('tipo_solicitacao.id'))
    nivel_usuario_id: Mapped[int] = mapped_column(
        ForeignKey('nivel_usuario.id'))
    usuario: Mapped['UsuarioModel'] = relationship(
        lazy='joined', foreign_keys=[usuario_id])
    tipo_solicitacao: Mapped['TipoSolicitacaoModel'] = relationship(
        lazy='joined', foreign_keys=[tipo_solicitacao_id])
    nivel_usuario: Mapped['NivelUsuarioModel'] = relationship(
        lazy='joined', foreign_keys=[nivel_usuario_id])


class TipoIntegracaoModel(settings.DBBaseModel):
    __tablename__ = 'tipo_integracao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    logo: Mapped[TEXT] = mapped_column(TEXT)
    nome: Mapped[str] = mapped_column(String(20))


class TipoSolicitacaoModel(settings.DBBaseModel):
    __tablename__ = 'tipo_solicitacao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(20))


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuario'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))
    cpf: Mapped[str] = mapped_column(String(15))
    email: Mapped[str] = mapped_column(String(50))
    senha: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(10))
    whatsapp: Mapped[str] = mapped_column(String(15))
    wizard: Mapped[bool] = mapped_column(Boolean)
    empresa_id: Mapped[int] = mapped_column(ForeignKey('empresa.id'))
    nivel_usuario_id: Mapped[int] = mapped_column(
        ForeignKey('nivel_usuario.id'))
    setor_id: Mapped[int] = mapped_column(ForeignKey('setor.id'))
    empresa: Mapped['EmpresaModel'] = relationship(
        lazy='joined', foreign_keys=[empresa_id])
    nivel_usuario: Mapped['NivelUsuarioModel'] = relationship(
        lazy='joined', foreign_keys=[nivel_usuario_id])
    setor: Mapped['SetorModel'] = relationship(
        lazy='joined', foreign_keys=[setor_id])
