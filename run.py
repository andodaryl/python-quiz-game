'''
This is the main app module to initiate startup.
'''
# Imports
import display_API as dis
import choice_API as choice
import question_API as quest
import score_API as score

# Data
app_status = {
  "active": True
}

# Behaviour
def main():
  dis.welcome_user()
  app_start_result = dis.request_app_start()
  app_status["active"] = choice.isYes(app_start_result)
  if not app_status["active"]: # Early exit
    dis.farewell_user()
    quit()
  question_list = quest.get_questions()
  for index in range(len(question_list)):
    question_tuple = question_list[index]
    question_number = index + 1
    current_question = question_tuple[0]
    correct_answer = question_tuple[1]
    user_answer = dis.request_user_answer(question_number=question_number, current_question=current_question)
    answer_is_correct = quest.is_answer_correct(user_answer=user_answer, correct_answer=correct_answer)
    if answer_is_correct:
      score.gain_reward()
  dis.game_over()
main()