numbers = [1, 2, 3, 4]

print(numbers)
print(type(numbers))

tasks = ['Do homework', 'do a dishes', 'play videogame']

print(tasks)
print(tasks[0])

# list with different types

types = [1, 'string', True]

print(types)
print(types[1])

# mutable

tasks[1] = 'Wash the dishes'

print(tasks)

# slicing

print(numbers[:3])

# operator in

print(True in types)  # True
print('hello' in types)  # False
