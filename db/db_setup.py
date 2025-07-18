from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "connect to db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
    )


#ASYNC ENGINE DATABASE CONNECTION
ASYNC_SQLALCHEMY_DATABASE_URL = "connect to db"

async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)

AsyncSessionLocal = sessionmaker(
    async_engine, class_ = AsyncSession, expire_on_commit=False
)
#---------------------------------------------


Base = declarative_base()

# #DB Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    
    

# DB Utilities for Async
async def async_get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()

