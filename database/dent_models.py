from pydantic import BaseModel


class QuestionsCountModel(BaseModel):
    questions_num: int

