from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from db.models.user import User
from pydantic_schemas.user import UserCreate


async def get_user(db: AsyncSession, user_id: int):
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()







