import random

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera => ').lower()

  if not user_option in options:
    print('Esa opcion no es valida')
    return None, None
    
  computer_option = random.choice(options)
  
  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  
  return user_option, computer_option

#---------------------------------------

def check_rules(user_option, computer_option, user_score, computer_score):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_score += 1
    else:
      print('papel gana a piedra')
      print('computer gano!')
      computer_score += 1
  elif user_option == 'tijera':
    if computer_option == 'piedra':
      print('piedra gana a tijera')
      print('computer gano!')
      computer_score += 1
    else:
      print('tijera gana a papel')
      print('user gano!')
      user_score += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano!')
      user_score += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_score += 1

  return user_score, computer_score

#--------------------------------------

def run_game():
  user_score = 0
  computer_score = 0
  rounds = 1
  
  while user_score < 2 or computer_score < 2:
  
    print('*' * 10)
    print('ROUND', rounds)
    print('USER', user_score)
    print('COMPUTER', computer_score)
    print('*' * 10)
  
    user_option, computer_option = choose_options()
    user_score, computer_score = check_rules(
      user_option,
      computer_option,
      user_score,
      computer_score
    )
  
    if user_score == 2:
      print("USER WIN")
      break
  
    if computer_score == 2:
      print("COMPUTER WIN")
      break
  
    rounds += 1

run_game()