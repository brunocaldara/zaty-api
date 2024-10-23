from datetime import datetime, timedelta
from typing import List, Optional

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import EmailStr
from pytz import timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.security import verify_password
from src.core.settings import settings
from src.models.usuario_model import UsuarioModel
