import html

class QuizBrain:
  """
  A class representing the logic for managing a quiz
  """

  def __init__(self, q_list):
    """
    Initializes the quiz brain with a list of questions

    Parameters:
    -q_list (list): List of Question objects representing the quiz questions
    """
    self.question_number = 0
    self.score = 0
    self.question_list = q_list
    self.current_question = None
  
  def still_has_questions(self):
    """
    checks if there are still questions remaining in the quiz
    """
    return self.question_number < len(self.question_list)
  
  def next_question(self):
    """
    retrieves the next question in the quiz
    
    Returns:
    - str: Formatted string representing the next question.
    """
    self.current_question = self.question_list[self.question_number]
    self.question_number += 1
    q_text = html.unescape(self.current_question.text)
    return f"Q.{self.question_number}: {q_text}"

  
  def check_answer(self, user_answer):
    """
    Checks if the provided user_answer matches the correct answer.

    Parameters:
    - user_answer (str): The user's answer.

    Returns:
    - bool: True if the answer is correct, False otherwise.
    """
    correct_answer = self.current_question.answer
    if user_answer.lower() == correct_answer.lower():
        self.score += 1
        return True
    else:
        return False
  
  