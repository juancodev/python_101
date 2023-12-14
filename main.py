import random

roundTotal = 3
options = ('piedra', 'papel', 'tijera')
scorePlayer = 0
scoreComputer = 0

for round in range(1, roundTotal + 1):
  if round <= roundTotal:
    print(f'------ Round {round} ------')
    user_option = input('piedra, papel o tijera => ').lower()
    if user_option not in options:
      print('Esa opcion no existe')
      continue

# random.choise(tuple) me permite elegir de forma aleatoria valores de una tuple
    computer_option = random.choice(options)
    if user_option == computer_option:
      print('¡Empate!')
      print(f'Puntaje => User: {scorePlayer} vs Computer: {scoreComputer}')
    elif user_option == 'piedra':
      if computer_option == 'tijera':
        scorePlayer += 1
        print('Piedra le gana a la tijera')
        print('¡User Ganó!')
        print(f'Puntaje => User: {scorePlayer} vs Computer: {scoreComputer}')
      else:
        scoreComputer += 1
        print('Papel le gana a la piedra')
        print('Computer Ganó')
        print(f'Puntaje => User: {scorePlayer} vs Computer: {scoreComputer}')
    elif user_option == 'papel':
      if computer_option == 'piedra':
        scorePlayer += 1
        print('Papel le gana a la piedra')
        print('¡User Ganó!')
        print(f'Puntaje => User: {scorePlayer} vs Computer: {scoreComputer}')
      else:
        scoreComputer += 1
        print('Tijera le gana a la papel')
        print('¡Computer Ganó!')
        print(f'Puntaje => User: {scorePlayer} vs Computer: {scoreComputer}')
    elif user_option == 'tijera':
      if computer_option == 'papel':
        scorePlayer += 1
        print('Tijera le gana a la papel')
        print('¡User Ganó!')
        print(f'Puntaje => User: {scorePlayer} vs Computer: {scoreComputer}')
      else:
        scoreComputer += 1
        print('Piedra le gana a la tijera')
        print('Computer Ganó')
        print(f'Puntaje => User: {scorePlayer} vs Computer: {scoreComputer}')

  if scorePlayer == 2 and scoreComputer == 0 or scoreComputer == 2 and scorePlayer == 0:
    break