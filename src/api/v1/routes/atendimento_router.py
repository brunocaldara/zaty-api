from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.database import get_session
from src.models import (AtendimentoModel, CanalModel, ConexaoModel,
                        EmpresaModel, SetorModel, UsuarioModel)
from src.schemas import AtendimentoSchema, AtendimentoSchemaBase

router = APIRouter()


async def validade_foreign_keys(atendimento: AtendimentoSchema, db: AsyncSession):
    if atendimento.empresa_id != None:
        query_empresa = select(EmpresaModel).filter(
            EmpresaModel.id == atendimento.empresa_id)
        result_empresa = await db.execute(query_empresa)
        empresa = result_empresa.scalar_one_or_none()

        if empresa == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Empresa inválida.')

    if atendimento.usuario_id != None:
        query_usuario = select(UsuarioModel).filter(
            UsuarioModel.id == atendimento.usuario_id)
        canal_result = await db.execute(query_usuario)
        canal = canal_result.scalar_one_or_none()

        if canal == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Usuário inválido.')

    if atendimento.conexao_id != None:
        query_canal = select(ConexaoModel).filter(
            ConexaoModel.id == atendimento.conexao_id)
        canal_result = await db.execute(query_canal)
        canal = canal_result.scalar_one_or_none()

        if canal == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Conexâo inválida.')

    if atendimento.setor_id != None:
        query_canal = select(SetorModel).filter(
            SetorModel.id == atendimento.setor_id)
        canal_result = await db.execute(query_canal)
        canal = canal_result.scalar_one_or_none()

        if canal == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Setor inválido.')

    if atendimento.canal_id != None:
        query_canal = select(CanalModel).filter(
            CanalModel.id == atendimento.canal_id)
        canal_result = await db.execute(query_canal)
        canal = canal_result.scalar_one_or_none()

        if canal == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Canal inválido.')


@router.get(path='/',
            description='Endpoint para recuperar todos os registros',
            summary=' ',
            response_model=List[AtendimentoSchema])
async def get_atendimentos(session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(AtendimentoModel)
        result = await db.execute(query)
        atendimentos: List[AtendimentoModel] = result.scalars().all()
        return atendimentos


@router.get(path='/{id}',
            description='Endpoint para recuperar registro pelo ID',
            summary=' ',
            response_model=AtendimentoSchema)
async def get_atendimento_by_id(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(AtendimentoModel).filter(AtendimentoModel.id == id)
        result = await db.execute(query)
        atendimento: List[AtendimentoModel] = result.scalar_one_or_none(
        )

        if atendimento == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Atendimento não encontrado.')
        return atendimento


@router.post(path='/',
             description='Endpoint para salvar novo registro',
             summary=' ',
             status_code=status.HTTP_201_CREATED,
             response_model=AtendimentoSchema)
async def post_atendimento(atendimento: AtendimentoSchemaBase, session: AsyncSession = Depends(get_session)):
    async with session as db:
        await validade_foreign_keys(atendimento, db)

        atendimento_insert: AtendimentoModel = AtendimentoModel()
        atendimento_insert.id_interno = atendimento.id_interno
        atendimento_insert.numero = atendimento.numero
        atendimento_insert.nome = atendimento.nome
        atendimento_insert.tipo_mensagem = atendimento.tipo_mensagem
        atendimento_insert.mensagem = atendimento.mensagem
        atendimento_insert.foto_perfil = atendimento.foto_perfil
        atendimento_insert.data_hora = atendimento.data_hora
        atendimento_insert.dispositivo = atendimento.dispositivo
        atendimento_insert.enviada_por_mim = atendimento.enviada_por_mim
        atendimento_insert.tipo_atendimento = atendimento.tipo_atendimento
        atendimento_insert.primeiro_registro = atendimento.primeiro_registro
        atendimento_insert.ultimo_registro = atendimento.ultimo_registro
        atendimento_insert.status = atendimento.status
        atendimento_insert.empresa_id = atendimento.empresa_id
        atendimento_insert.usuario_id = atendimento.usuario_id
        atendimento_insert.conexao_id = atendimento.conexao_id
        atendimento_insert.setor_id = atendimento.setor_id
        atendimento_insert.canal_id = atendimento.canal_id
        db.add(atendimento_insert)
        await db.commit()
        return atendimento_insert


@router.put(path='/{id}',
            description='Endpoint para atualizar registro pelo ID',
            summary=' ',
            status_code=status.HTTP_202_ACCEPTED,
            response_model=AtendimentoSchema)
async def put_atendimento(id: int, atendimento: AtendimentoSchemaBase, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(AtendimentoModel).filter(AtendimentoModel.id == id)
        result = await db.execute(query)
        atendimento_update = result.scalar_one_or_none()

        if atendimento_update == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Atendimento não encontrado.')
        else:
            await validade_foreign_keys(atendimento, db)

            atendimento_update.id_interno = atendimento.id_interno
            atendimento_update.numero = atendimento.numero
            atendimento_update.nome = atendimento.nome
            atendimento_update.tipo_mensagem = atendimento.tipo_mensagem
            atendimento_update.mensagem = atendimento.mensagem
            atendimento_update.foto_perfil = atendimento.foto_perfil
            atendimento_update.data_hora = atendimento.data_hora
            atendimento_update.dispositivo = atendimento.dispositivo
            atendimento_update.enviada_por_mim = atendimento.enviada_por_mim
            atendimento_update.tipo_atendimento = atendimento.tipo_atendimento
            atendimento_update.primeiro_registro = atendimento.primeiro_registro
            atendimento_update.ultimo_registro = atendimento.ultimo_registro
            atendimento_update.status = atendimento.status
            atendimento_update.empresa_id = atendimento.empresa_id
            atendimento_update.usuario_id = atendimento.usuario_id
            atendimento_update.conexao_id = atendimento.conexao_id
            atendimento_update.setor_id = atendimento.setor_id
            atendimento_update.canal_id = atendimento.canal_id
            await db.commit()
            return atendimento_update


@router.delete(path='/{id}',
               description='Endpoint para excluir registro pelo ID',
               summary=' ',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_atendimento(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(AtendimentoModel).filter(AtendimentoModel.id == id)
        result = await db.execute(query)
        atendimento_delete = result.scalar_one_or_none()

        if atendimento_delete == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Atendimento não encontrado.')
        else:
            await db.delete(atendimento_delete)
            await db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
