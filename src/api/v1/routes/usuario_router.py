# import hashlib
# m = hashlib.sha512()
# m.update(b"123")
# m.hexdigest()

from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.auth import autenticate_user, create_jwt_token, get_current_user
from src.core.database import get_session
from src.models.usuario_model import UsuarioModel
from src.schemas.usuario_schema import UsuarioSchema, UsuarioSchemaCreate

router = APIRouter()


@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)):
    usuario = await autenticate_user(form_data.username, form_data.password, session)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Credenciais inválidas.')

    return JSONResponse(content={'access_token': create_jwt_token(usuario.id),
                                 'token_type': 'bearer'}, status_code=status.HTTP_200_OK)
