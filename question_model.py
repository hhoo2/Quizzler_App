class Question:
  """
  A class representing a quiz question.
  """
  
  def __init__(self, q_text, q_answer):
    """
    Initializes a Question object with the provided text and answer.

    Parameters:
    - q_text (str): The text of the question.
    - q_answer (str): The correct answer to the question.
    """
    self.text = q_text
    self.answer = q_answer