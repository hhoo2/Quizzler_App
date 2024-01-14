from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
  """
    A class representing the graphical user interface for the quiz application.

    Attributes:
    - quiz (QuizBrain): An instance of the QuizBrain class for managing the quiz logic.
    - window (Tk): The main window of the GUI.
    - score_label (Label): Label displaying the current score.
    - canvas (Canvas): Canvas for displaying quiz questions.
    - question_text (int): Text object on the canvas for displaying the question.
    - true_button (Button): Button for selecting True as an answer.
    - false_button (Button): Button for selecting False as an answer.
    """

  def __init__(self, quiz_brain: QuizBrain):
    """
        Initializes a QuizInterface object.

        Parameters:
        - quiz_brain (QuizBrain): An instance of the QuizBrain class for managing the quiz logic.
        """
    self.quiz = quiz_brain
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    # Label for displaying the current score
    self.score_label = Label(text="Score: 0/10", fg="white", bg=THEME_COLOR)
    self.score_label.grid(row=0, column=1)

    # Canvas for displaying quiz questions
    self.canvas = Canvas(width=300, height=250, bg="white")
    self.question_text = self.canvas.create_text(
        150,
        125,
        width=280,  # wrap the text to fit the canvas
        text="Some Question Text",
        fill=THEME_COLOR,
        font=("Arial", 20, "italic"))
    self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    # True button
    true_image = PhotoImage(file="images/true.png")
    self.true_button = Button(image=true_image,
                              highlightthickness=0,
                              command=self.true_pressed)
    self.true_button.grid(row=2, column=0)

    # False button
    false_image = PhotoImage(file="images/false.png")
    self.false_button = Button(image=false_image,
                               highlightthickness=0,
                               command=self.false_pressed)
    self.false_button.grid(row=2, column=1)

    # Get the first question
    self.get_next_question()

    # Start the main event loop
    self.window.mainloop()

  def get_next_question(self):
    """
        Gets the next question from the quiz and updates the GUI accordingly.
        """
    self.canvas.config(bg="white")
    if self.quiz.still_has_questions():
      self.canvas.config(bg="white")
      self.score_label.config(text=f"Score: {self.quiz.score}/10")
      q_text = self.quiz.next_question()
      self.canvas.itemconfig(self.question_text, text=q_text)
    else:
      self.canvas.itemconfig(
          self.question_text,
          text="You've reached the end of the quiz. Good job!:) ")
      self.true_button.config(state="disabled")
      self.false_button.config(state="disabled")

  def true_pressed(self):
    """
        Handles the event when the True button is pressed.
        """
    self.give_feedback(self.quiz.check_answer("True"))

  def false_pressed(self):
    """
        Handles the event when the False button is pressed.
        """
    self.give_feedback(self.quiz.check_answer("False"))

  def give_feedback(self, is_right):
    """
        Provides feedback based on whether the answer is correct and updates the GUI.

        Parameters:
        - is_right (bool): True if the answer is correct, False otherwise.
        """
    if is_right:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    # After 1000 milliseconds (1 second), get the next question
    self.window.after(1000, self.get_next_question)
