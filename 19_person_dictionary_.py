person = {
  'name': 'Juan Carlos',
  'lastName': 'Montilla Sanchez',
  'age': 25,
  'profession': 'Developer',
  'languages': ['JavaScript', 'Python', 'Node']
}

print(type(person))
print(person)

# add values

print('ADD VALUE 👇🏼')
person['country'] = 'Venezuela'
person['city'] = 'Caracas'
person['languages'].append('C#')

print(person)

# modified values

print('MODIFIED VALUE 👇🏼')
person['age'] -= 1
print(person)

# delete value

print('DELETE VALUE 👇🏼')
del person['city']
print(person)

# other method for delete a value
person.pop('country')
print(person)

# items of the dictionary: key and value
print('ITEMS 👇🏼')
print(person.items())

# keys of the dictionary: only key
print('KEYS 👇🏼')
print(person.keys())

# values of the dictionary: only values
print('VALUES')
print(person.values())