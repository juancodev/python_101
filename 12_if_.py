'''
pet = input('What is your pet? => ')
if pet == 'dog':
  print('Your pet is great!!')
elif pet == 'cat':
  print('Your pet is very nice!!')
elif pet == 'fish':
  print('Your pet is very interesting')
else:
  print('Your pet is awesome!!')
'''

#### Challange

number = int(input('Ingrese un número => '))

if number % 2 == 0:
  print('Numero par')
else:
  print('Numero inpar')

camisa = input('Ingresa la marca de la camisa a buscar => ').lower()

if camisa == 'adidas':
  print('Sí hay esa camisa => ', camisa)
else:
  print('No hay esa marca de la camisa => ', camisa)
