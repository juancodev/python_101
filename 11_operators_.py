# AND
print('AND')
print('True and True: =>', True and True)

stock = input('Ingrese el número de stock => ')
stock = int(stock)

print(stock > 0 and stock <= 100)

# OR

print('OR')
print('True or True: => ', True or True)

role = input('What is your role? => ')
print(role == 'admin' or role == 'seller')

# NOT

print('NOT')
print('not (True and True) => ', not(True and True))