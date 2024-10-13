from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database.database import Base

class Experiment(Base):
    __tablename__ = 'experiments'

    id = Column(Integer, primary_key=True, index=True)
    theme_id = Column(Integer, ForeignKey('themes.id'))
    title = Column(String)
    description = Column(Text)
    parameters = Column(JSON)
    updated_at = Column(TIMESTAMP, nullable=False)

    theme = relationship('Theme', back_populates='experiments')
    creator = relationship('User', back_populates='experiments')