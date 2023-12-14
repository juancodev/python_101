# Las tuplas solamente me permite crear pero no puedo mutar

numbers = (1, 2, 3, 4)
print(numbers)
print(type(numbers))
strings = ('juan', 'cynthia', 'maria', 'maria')

# Methods

print(strings.index('cynthia'))
print(strings.count('maria')) # saber cuántas coincidencias hay

# convertion
my_list = list(strings)
my_list[0] = 'Juan'
print(my_list)
print(type(my_list))

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))