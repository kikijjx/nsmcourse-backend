from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database.database import Base

class Theme(Base):
    __tablename__ = 'themes'

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    creator_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    description = Column(Text)
    content = Column(JSON)
    updated_at = Column(TIMESTAMP, nullable=False)

    course = relationship('Course', back_populates='themes')
    creator = relationship('User', back_populates='themes')
    experiments = relationship('Experiment', back_populates='theme')
