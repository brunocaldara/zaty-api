from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    create_async_engine)
from sqlalchemy.orm import sessionmaker

from core.settings import settings

engine: AsyncEngine = create_async_engine(
    settings.DB_URL
)

Session: AsyncSession = sessionmaker(
    expire_on_commit=False,
    autoflush=False,
    class_=AsyncSession,
    bind=engine
)


async def get_session() -> AsyncGenerator:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()


# class DbConnection():
#     def __init__(self) -> None:
#         self.__DB_URL = 'postgresql+asyncpg://postgres:PWMxXt7uiR9ALeMcXigd@95.216.214.177:5432/zaty'
#         self.__engine = self.__create_database_engine()
#         self.session = None

#     def __create_database_engine(self):
#         engine: AsyncEngine = create_async_engine(
#             self.__DB_URL
#         )
#         return engine

#     def get_engine(self):
#         return self.__engine

#     def __enter__(self):
#         print('enter')
#         Session: AsyncSession = sessionmaker(
#             expire_on_commit=False,
#             autoflush=False,
#             class_=AsyncSession,
#             bind=self.__engine
#         )
#         self.session = Session()
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#         self.session.close()


# if __name__ == '__main__':
#     with DbConnection() as db:
#         print('Criou')
