'''
Module for question generator and related behaviour.
'''
# Import
from random import randint

# Behaviour
max_questions = 10

get_random_number = lambda: (randint(-1000, 1000))
question_type = (
  lambda a=get_random_number(), b=get_random_number(): (f"{a} + {b} = ", a + b), # add
  lambda a=get_random_number(), b=get_random_number(): (f"{a} - {b} = ", a - b), # minus
  lambda a=get_random_number(), b=get_random_number(): (f"{a} x {b} = ", a * b), # multiply
  lambda a=get_random_number(), b=get_random_number(): (f"{a*b} / {a} = ", b), # divide
)
get_random_question = lambda: question_type[randint(0, len(question_type) - 1)]
generate_question = lambda get_generator=get_random_question(): get_generator()

get_questions = lambda total=max_questions: tuple([generate_question() for question_number in range(total)])