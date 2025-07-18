import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null 
from .mixins import Timestamp

from ..db_setup import Base


class Role(enum.IntEnum):
    Teacher = 1
    Student = 2

class User(Timestamp, Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))
    is_active = Column(Boolean, default=False)

    profile = relationship("Profile", back_populates="owner", uselist=False)
    student_courses = relationship("StudentCourse", back_populates="student")
    student_content_blocks = relationship("CompletedContentBlock", back_populates="student")

class Profile(Timestamp, Base):
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    bio = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="profile")





