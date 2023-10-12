from fastapi import FastAPI, Body, Depends
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from database import models
from database.questionservice import add_new_questions
from database.dent_models import QuestionsCountModel
from utils import get_q_from_url

Base.metadata.create_all(bind=engine)


app = FastAPI(docs_url='/')
test_url = 'https://jservice.io/api/random?count={amount}'


# Запрос на получение вопроса
@app.post('/questions')
async def get_questions(questions_num: QuestionsCountModel = Body(...),
                        db: Session = Depends(get_db)):
    # Отправляем запрос на публичный API
    questions = await get_q_from_url(test_url, questions_num.questions_num)

    # Сохраняем в базу
    status = add_new_questions(db, questions)
    result = status['questions']

    # Отправляем доп запрос если в базе уже есть текущй вопрос
    while status['not_new_questions'] != 0:
        questions = await get_q_from_url(test_url, status)
        status = add_new_questions(db, questions)
        result.extend(status['questions'])

    return {'question': result}
