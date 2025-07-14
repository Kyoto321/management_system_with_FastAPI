from typing import Optional, List
from fastapi import Path, Query, APIRouter
from pydantic import BaseModel

router = APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@router.get("/users", response_model=List[User])
async def get_users():
    return users

@router.post("/create_users")
async def create_users(user: User):
    users.append(user)
    return "Success"

@router.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="Provide the user Id", gt=2),
    q: str = Query(None, max_length=5)
    ):
    return {"users": users[id], "query": q }
