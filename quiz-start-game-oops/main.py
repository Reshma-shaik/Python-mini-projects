# TODO: inline comments and doc-strings to be updated
from data import questions
from quiz_brain import QuizBrain
from question_model import Question

questions_list = [Question(q["text"], q["answer"]) for q in questions]

quiz_brain = QuizBrain(questions_list)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"Your Quiz is completed\nAnd here is your score: {quiz_brain.score}")
