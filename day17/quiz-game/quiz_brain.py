class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.user_score = 0
        self.question_list = question_list

    def quiz_not_finished(self):
        total_questions = len(self.question_list)
        if self.question_number < total_questions:
            return True
        else:
            return False

    def increase_score(self):
        self.user_score += 1

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
        if user_answer == self.question_list[self.question_number].answer:
            return True
        else:
            return False

    def evaluate_answer(self):
        if self.next_question():
            print("You got it right!")
            print("The correct answer was: {}")
            self.increase_score()
            print(f"Your current score is: {self.user_score}")
        else:
            print("You got it right!")
            print("The correct answer was: {}")
            print(f"Your current score is: {self.user_score}")
        if self.question_number == len(self.question_list):
            quiz_running = False
