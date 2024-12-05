from question_model import Question
from data import question_data
from quiz_brain import Quizbrain
Question_bank = []
for i in question_data:
    Question_bank.append(Question(qtext=i['question'], qanswer=i['correct_answer']))


quiz = Quizbrain(Question_bank)


while quiz.still_has_questions():
    quiz.next_question()
print("you've completed the quiz.")
print(f"The final score is {quiz.score}/{quiz.Question_number}")
