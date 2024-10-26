from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel, EmailStr
from pytz import timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.database import get_session
from src.core.security import verify_password
from src.core.settings import settings
from src.models.usuario_model import UsuarioModel

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_URL_VERISON}/auth/token'
)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


async def autenticate_user(email: EmailStr, password: str, session: AsyncSession) -> Optional[UsuarioModel]:
    async with session as db:
        query = select(UsuarioModel).filter(UsuarioModel.email == email)
        result = await db.execute(query)
        usuario: UsuarioModel = result.scalar_one_or_none()

        if not usuario:
            return None

        if not verify_password(password, usuario.senha):
            return None

        return usuario


def create_jwt_token(sub: str) -> str:
    payload = {}
    datetime_now = datetime.now(tz=timezone('America/Sao_Paulo'))
    expires = datetime_now + timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    payload['type'] = 'access_token'
    payload['exp'] = expires
    payload['iat'] = datetime_now
    payload['sub'] = sub

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)


async def get_current_user(
    session: AsyncSession = Depends(get_session),
    token: str = Depends(oauth2_schema)
) -> UsuarioModel:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Credenciais inválidas',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[
                             settings.JWT_ALGORITHM], options={'verify_aud': False})
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception

        token_data: TokenData = TokenData(username)
    except JWTError:
        raise credentials_exception

    async with session as db:
        query = select(UsuarioModel).filter(
            UsuarioModel.id == int(token_data.username))
        result = await db.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()

        if not usuario:
            raise credentials_exception

        return usuario
