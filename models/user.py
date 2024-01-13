from sqlalchemy import Boolean, Column, Integer, String

from database import Base

class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    firstName: str = Column(String(50), index=True)
    lastName: str = Column(String(50), index=True)
    middleName: str = Column(String(50), index=True)
    position: str = Column(String(50), index=True)