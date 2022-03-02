'''
Module for question generator and related behaviour.
'''
# Import
from random import randint
from random import choice as get_random_item

# Behaviour
max_questions = 10

get_random_number = lambda: (randint(-1000, 1000))
question_type = (
  lambda a=get_random_number(), b=get_random_number(): (f"{a} + {b} = ?", a + b), # add
  lambda a=get_random_number(), b=get_random_number(): (f"{a} - {b} = ?", a - b), # minus
  lambda a=get_random_number(), b=get_random_number(): (f"{a} x {b} = ?", a * b), # multiply
  lambda a=get_random_number(), b=get_random_number(): (f"{a*b} / {a} = ?", b), # divide
)

generate_question = lambda: get_random_item(question_type)()

get_questions = lambda total=max_questions: tuple([generate_question() for question_number in range(total)])

is_answer_correct = lambda user_answer=None, correct_answer=None: user_answer == correct_answer if type(user_answer) is int else False