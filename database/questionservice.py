from sqlalchemy.orm import Session
from datetime import datetime
from database.models import Question


# Добавление вопросов в базу
def add_new_questions(db: Session, questions: list[dict]) -> dict:
    not_new_questions = 0
    new_questions = []

    for question in questions:
        question_id = question['id']
        existing_questions = db.query(Question.question_id).filter_by(question_id=question_id).first()

        # Если вопроса нет в базе, то добавляем
        if not existing_questions:
            question['created_at'] = datetime.strptime(question['created_at'], "%Y-%m-%dT%H:%M:%S.%f%z")
            new_question = Question(question_id=question_id, question_text=question['question'],
                                    game_id=question['game_id'], answer=question['answer'], value=question['value'],
                                    created_at=question['created_at'])
            new_questions.append(new_question)

        else:
            not_new_questions += 1

    db.add_all(new_questions)
    db.commit()

    return {'not_new_questions': not_new_questions,
            'questions': [i.question_text for i in new_questions]}
