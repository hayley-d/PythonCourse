from data import question_data
from question_model import  Question
from quiz_brain import QuizBrain


questions = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    questions.append(new_question)

quiz = QuizBrain(questions)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You completed the quiz! with a score of {quiz.get_score()}")