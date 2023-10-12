from sqlalchemy import Column, String, Integer, DateTime
from database import Base


class Question(Base):
    __tablename__ = 'questions'
    question_id = Column(Integer, primary_key=True, unique=True)
    game_id = Column(Integer)
    question_text = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    value = Column(Integer)

    created_at = Column(DateTime)


