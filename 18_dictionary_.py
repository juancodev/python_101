# list = []
# tuple = ()
# dictionary = {}

my_dictionary = {}
print(type(my_dictionary))

my_dictionary = {
  'key': "Value",
  'name': "Juan Carlos",
  'lastName': "Montilla Sanchez",
  'age': "25"
}

print(my_dictionary)

# longitud
print(len(my_dictionary))

# get values
print(my_dictionary['name'])
print(my_dictionary['lastName'])

# Este me permite obtener un valor y si no existe no se rompe la ejecución
print(my_dictionary.get('age'))

print('name' in my_dictionary)