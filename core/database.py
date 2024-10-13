from typing import AsyncGenerator, Generator

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
