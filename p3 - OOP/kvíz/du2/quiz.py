from data_quiz import question_data
from questionmodel import Question
from QuizBrain import QuizBrain
question_list = []

for one_question in question_data:
    question = one_question ["text"]
    answer = one_question ["answer"]
    new_question = Question(question, answer)
    question_list.append(new_question)


quiz = QuizBrain(question_list)

while quiz.has_question() == True:
    quiz.next_question()
    

print("Dokončili jste kvíz!.")
