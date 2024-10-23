import os
from typing import Any, Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()


class Settings(BaseSettings):
    '''
    Configurações Gerais usada na API
    '''
    API_URL_VERISON: str = '/api/v1'
    API_VERSION: str = '0.0.1'

    DB_HOST: Optional[str] = os.getenv('DB_HOST')
    DB_NAME: Optional[str] = os.getenv('DB_NAME')
    DB_PORT: Optional[str] = os.getenv('DB_PORT')
    DB_USER: Optional[str] = os.getenv('DB_USER')
    DB_PASS: Optional[str] = os.getenv('DB_PASS')
    DB_URL: str = f'postgresql+asyncpg://{DB_USER}:{
        DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    DBBaseModel: Any = declarative_base()

    '''
    openssl rand -hex 32
    '''
    JWT_SECRET: str = '60fb77f73db2a2cd5e50dfddcf2d8f5b1dd9a1ebf7f307442d24871b988053e6'
    JWT_ALGORITHM: str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    JWT_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings = Settings()
