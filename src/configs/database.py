from src.configs.env import DATABASE_URL

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

engine = create_async_engine(DATABASE_URL)

AsyncSessionLocal = async_sessionmaker(engine, class_ = AsyncSession, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as db:
        yield db