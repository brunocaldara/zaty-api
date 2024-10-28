from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.auth import autenticate_user, create_jwt_token, get_current_user
from src.core.database import get_session
from src.core.security import generate_password_hash, verify_password
from src.models import EmpresaModel, UsuarioModel
from src.schemas import (NivelUsuarioSchema, SetorSchema, UsuarioSchema,
                         UsuarioSchemaBase, UsuarioSchemaChangePassword,
                         UsuarioSchemaCreate)

router = APIRouter()


async def validade_foreign_keys(usuario: UsuarioSchemaCreate, db: AsyncSession):
    if usuario.empresa_id != None:
        query_empresa = select(EmpresaModel).filter(
            EmpresaModel.id == usuario.empresa_id)
        result_empresa = await db.execute(query_empresa)
        empresa = result_empresa.scalar_one_or_none()

        if empresa == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Empresa inválida.')

    if usuario.nivel_usuario_id != None:
        query_nivel_usuario = select(NivelUsuarioSchema).filter(
            NivelUsuarioSchema.id == usuario.nivel_usuario_id)
        result_nivel_usuario = await db.execute(query_nivel_usuario)
        nivel_usuario = result_nivel_usuario.scalar_one_or_none()

        if nivel_usuario == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Nível Usuário inválido.')

    if usuario.setor_id != None:
        query_setor = select(SetorSchema).filter(
            SetorSchema.id == usuario.setor_id)
        result_setor = await db.execute(query_setor)
        setor = result_setor.scalar_one_or_none()

        if setor == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Setor inválido.')


@router.post(path='/login',
             description='Endpoint para obter o token de autenticação',
             summary=' ',
             response_model=List[UsuarioSchema])
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)):
    usuario = await autenticate_user(form_data.username, form_data.password, session)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Credenciais inválidas.')

    return JSONResponse(content={'access_token': create_jwt_token(usuario.id),
                                 'token_type': 'bearer'}, status_code=status.HTTP_200_OK)


@router.get(path='/',
            description='Endpoint para recuperar todos os registros',
            summary=' ',
            response_model=List[UsuarioSchema])
async def get_usuarios(session: AsyncSession = Depends(get_session),
                       usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with session as db:
        query = select(UsuarioModel)
        result = await db.execute(query)
        usuarios: List[UsuarioModel] = result.scalars().all()
        return usuarios


@router.get(path='/{id}',
            description='Endpoint para recuperar registro pelo ID',
            summary=' ',
            response_model=UsuarioSchema)
async def get_usuario_by_id(id: int, session: AsyncSession = Depends(get_session),
                            usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with session as db:
        query = select(UsuarioModel).filter(
            UsuarioModel.id == id)
        result = await db.execute(query)
        usuario: List[UsuarioModel] = result.scalar_one_or_none(
        )

        if usuario == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Usuário não encontrado.')

        return usuario


@router.post(path='/',
             description='Endpoint para salvar novo registro',
             summary=' ',
             status_code=status.HTTP_201_CREATED,
             response_model=UsuarioSchema)
async def post_usuario(usuario: UsuarioSchemaCreate,
                       session: AsyncSession = Depends(get_session),
                       usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with session as db:
        validade_foreign_keys(usuario, db)

        usuario_insert: UsuarioModel = UsuarioModel()
        usuario_insert.nome = usuario.nome
        usuario_insert.senha = generate_password_hash(usuario.senha)
        usuario_insert.cpf = usuario.cpf
        usuario_insert.whatsapp = usuario.whatsapp
        usuario_insert.email = usuario.email
        usuario_insert.status = usuario.status
        usuario_insert.empresa_id = usuario.empresa_id
        usuario_insert.nivel_usuario_id = usuario.nivel_usuario_id
        usuario_insert.wizard = usuario.wizard
        usuario_insert.setor_id = usuario.setor_id
        db.add(usuario_insert)
        await db.commit()
        return usuario_insert


@router.put(path='/{id}',
            description='Endpoint para atualizar registro pelo ID',
            summary=' ',
            status_code=status.HTTP_202_ACCEPTED,
            response_model=UsuarioSchema)
async def put_usuario(id: int, usuario: UsuarioSchemaBase,
                      session: AsyncSession = Depends(get_session),
                      usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with session as db:
        query = select(UsuarioModel).filter(
            UsuarioModel.id == id)
        result = await db.execute(query)
        usuario_update = result.scalar_one_or_none()

        if usuario_update == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Usuário não encontrado.')
        else:
            await validade_foreign_keys(usuario, db)

            usuario_update.nome = usuario.nome
            usuario_update.cpf = usuario.cpf
            usuario_update.whatsapp = usuario.whatsapp
            usuario_update.email = usuario.email
            usuario_update.status = usuario.status
            usuario_update.empresa_id = usuario.empresa_id
            usuario_update.nivel_usuario_id = usuario.nivel_usuario_id
            usuario_update.wizard = usuario.wizard
            usuario_update.setor_id = usuario.setor_id
            await db.commit()
            return usuario_update


@router.delete(path='/{id}',
               description='Endpoint para excluir registro pelo ID',
               summary=' ',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(id: int, session: AsyncSession = Depends(get_session),
                         usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with session as db:
        query = select(UsuarioModel).filter(
            UsuarioModel.id == id)
        result = await db.execute(query)
        usuario_delete = result.scalar_one_or_none()

        if usuario_delete == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Usuário não encontrado.')
        else:
            await db.delete(usuario_delete)
            await db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post(path='/trocar-senha',
             description='Endpoint para trocar senha',
             summary=' ',
             status_code=status.HTTP_202_ACCEPTED,
             response_model=UsuarioSchemaChangePassword)
async def post_usuario_change_password(usuario: UsuarioSchemaChangePassword,
                                       session: AsyncSession = Depends(
                                           get_session),
                                       usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with session as db:
        query = select(UsuarioModel).filter(
            UsuarioModel.email == usuario.email)
        result = await db.execute(query)
        usuario_change_password = result.scalar_one_or_none()

        if usuario_change_password == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Usuário não encontrado.')
        else:
            if (usuario_change_password.id != usuario_logado.id
                    and usuario_logado.nivel_usuario_id == 4):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail='Usuário logado não tem permissão para trocar a senha.')

            if not verify_password(usuario.senha_atual, usuario_change_password.senha):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail='Senha inválida.')

            usuario_change_password.senha = generate_password_hash(
                usuario.senha_nova)
            await db.commit()
            return Response(status_code=status.HTTP_200_OK)
