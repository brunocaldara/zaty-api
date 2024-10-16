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

    class Config:
        case_sensitive = True


settings = Settings()
