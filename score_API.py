'''
API for points related behaviour.
'''

# Imports
from question_API import max_questions

# Data
reward_per_question = 1
max_reward = max_questions * reward_per_question
current_score = 0

# Behaviour
show_points = lambda: current_score

calculate_reward = lambda weight=1: reward_per_question * weight

def gain_reward():
  current_score += calculate_reward()