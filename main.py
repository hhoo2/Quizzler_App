#importing necessary modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

#creating an empty list to store Question objects
question_bank = []

#Populating the question bank list with Question objects
for question in question_data:
  question_text = question["question"]
  question_answer = question["correct_answer"]
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)

#Creating a QuizBrain object with the populated question_bank
quiz = QuizBrain(question_bank)

#Creating a QuizInterface object with the quiz as an argument
quiz_ui = QuizInterface(quiz)

#Printing completion message and final score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")