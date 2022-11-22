from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

quiz = quiz = QuizBrain(question_bank)

while quiz.quiz_not_finished():
    quiz.next_question()