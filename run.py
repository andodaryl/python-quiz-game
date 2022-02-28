'''
This is the main app module to initiate startup.
'''
# Imports
import display_API as dis
import choice_API as choice

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
main()