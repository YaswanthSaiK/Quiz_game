

class Quizbrain:
    def __init__(self, qlist):
        self.Question_number = 0
        self.question_list = qlist
        self.score = 0

    def still_has_questions(self):
        if self.Question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.Question_number]
        a = input(f'q.{self.Question_number+1} {current_question.text} True/False: ')
        self.Question_number += 1
        if current_question.answer.lower() != a.lower():
            print(f"you got it wrong, sorry!Your score is {self.score}/{self.Question_number}")
        else:
            self.score += 1
            print(f"you got it right!Your score is {self.score}/{self.Question_number}")
        print("\n")


