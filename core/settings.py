import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()


class Settings(BaseSettings):
    '''
    Configurações Gerais usada na API
    '''
    API_URL_VERISON: str = '/api/v1'
    DB_HOST: str = os.getenv('DB_HOST')
    DB_NAME: str = os.getenv('DB_NAME')
    DB_PORT: str = os.getenv('DB_PORT')
    DB_USER: str = os.getenv('DB_USER')
    DB_PASS: str = os.getenv('DB_PASS')
    DB_URL: str = f'postgresql+asyncpg://{DB_USER}:{
        DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
