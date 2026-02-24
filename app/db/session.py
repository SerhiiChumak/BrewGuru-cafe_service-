# cafe_service/app/db/session.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from cafe_service.app.core.config import settings

# Використовуємо 127.0.0.1 для локального запуску, щоб уникнути помилок DNS
engine = create_async_engine(settings.DATABASE_URL, echo=True)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with async_session() as session:
        yield session
