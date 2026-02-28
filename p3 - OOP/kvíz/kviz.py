from data_quiz import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_list = []

for one_question in question_data:
    question_t = one_question["question"]
    question_a = one_question["correct_answer"]
    new_question = Question(question_t, question_a)
    question_list.append(new_question)


quiz = QuizBrain(question_list)

# True není potřebné, jen pro vysvětlení.
while quiz.has_question() == True:
    quiz.next_question()
print("Dokončili jste kvíz")
print(f"Vaše celkové skóre je {quiz.score} / {quiz.question_number}")