# for loop
''' range
for i in range(10):
  print(i)
'''
''' range  from 1 to 11
for element in range(1, 11):
  print(element)
'''
''' List
my_list = [10, 20, 30, 40, 50, 60]

for i in my_list:
  print(i)
'''
''' Tuple
my_tuple = ('Juan', 'Carlos', 'Cynthia')

for i in my_tuple:
  print(i)
'''

# dictionary
product = {'name': 'Shirt', 'price': 100, 'stock': 80}

for i in product:
  print(product[i])

for key, value in product.items():
  print(key, '=>', value)

people = [{
  'name': 'Juan',
  'age': 25
}, {
  'name': 'Cynthia',
  'age': 24
}, {
  'name': 'Vicente',
  'age': 27
}]

for person in people:
  print(person)

for person in people:
  print('name => ', person['name'], ' age => ', person['age'])