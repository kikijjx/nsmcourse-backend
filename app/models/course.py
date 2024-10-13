from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)

    themes = relationship('Theme', back_populates='course')