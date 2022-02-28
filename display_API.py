'''
API for display related behaviour.
'''

# Imports
from pprint import pprint

# Data
input_type = {
  "yes" : 'Y',
  "no" : 'N',
}

display = {
  "welcome_message" : "Hello, are you ready for a maths quiz?",
  "yes_or_no": f"Yes = {input_type['yes']} \n No = {input_type['no']}'"
}

# Behaviour
print(display["welcome_message"])

app_start_request = input(f"Start quiz?\n{display['yes_or_no']}\n")

app_inactive = lambda app_start_request : app_start_request != display["input_yes"]

if app_inactive:
  quit()