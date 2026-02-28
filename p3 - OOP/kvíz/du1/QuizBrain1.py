class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
    
    def next_question (self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Otázka č. {self.question_number} je {current_question.text}")
        self.checker(user_input, current_question.answer)

    def checker (self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Uhádli jste!")
            self.score += 1
        else:
            print("Špatná odpověď.")
        print(f"Správná odpověď je {correct_answer}")
        print(f"Vaše skore je {self.score} / {self.question_number}")

    def has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False