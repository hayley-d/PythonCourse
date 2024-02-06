
class QuizBrain:
    def __init__(self,question_list,question_num = 0, score = 0):
        self.question_num = 0
        self.score = 0
        self.question_list = question_list




    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def check_answer(self, correct_ans,user_ans):
        return correct_ans.lower() == user_ans.lower()

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {current_question.question_text} (True/False): ")
        checked = self.check_answer(current_question.answer, user_answer)
        if checked:
            self.score += 1
            print(f"Correct answer: {current_question.answer}")
        else:
            print(f"Incorrect answer :(")
        print(f"Your score is {self.score}/{self.question_num}\n")

    def get_score(self):
        return self.score