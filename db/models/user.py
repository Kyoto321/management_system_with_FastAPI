import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null 
from .mixins import Timestamp

from ..db_setup import Base


class Role(enum.Enum):
    Teacher = 1
    Student = 2

class User(Timestamp, Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))
    profile = relationship("Profile", back_populates="owner", uselist=False)


class UserProfile(Timestamp, Base):
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    bio = Column(String(100), nullable=False)
    is_active = Column(Boolean, default = False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    owner = relationship("User", back_populates="profile")





