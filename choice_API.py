'''
API for user input related behaviour.
'''
# Data
choice_type = {
  "YES" : 'Y',
  "NO" : 'N',
}

isYes = lambda choice: choice.upper() == choice_type["YES"] if type(choice) is str else False