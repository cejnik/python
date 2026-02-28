from data_quiz1 import question_data
from question_model1 import Question
from QuizBrain1 import QuizBrain

question_list = []

for one_question in question_data:
    question_text = one_question["text"]
    question_answer = one_question["answer"]
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)

quiz = QuizBrain(question_list)
while quiz.has_question() == True:
    quiz.next_question()
print("Dokončili jste kvíz")
print(f"Máte {quiz.score} / {quiz.question_number}")