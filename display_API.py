'''
API for display related behaviour.
'''

# Imports
from choice_API import choice_type
from question_API import is_answer_correct

# Data
display = {
  "input_mark": ">>> ",
  "welcome_message" : "Hello, are you ready for a maths quiz?",
  "goodbye_message": "Goodbye, see you next time!",
  "yes_or_no": f"Yes = {choice_type['YES']} No = {choice_type['NO']}",
  "yes_to_continue": f"Enter '{choice_type['YES']}' to continue",
}

# Behaviour
welcome_user = lambda: print(f"{display['welcome_message']} {display['input_mark']}")

farewell_user = lambda: print(f"{display['goodbye_message']} {display['input_mark']}")

request_app_start = lambda: input(f"{display['yes_to_continue']} {display['input_mark']}")

request_user_answer = lambda question_number=0, current_question="a + b = ?": input(f"{str(question_number)}: {current_question} {display['input_mark']}")