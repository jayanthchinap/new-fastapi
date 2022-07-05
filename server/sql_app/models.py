from sqlalchemy import DATE, Boolean, Column, ForeignKey, Integer, String

from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    lastName = Column(String)
    DOB = Column(String)
    skill = Column(String)
    available = Column(String)
  