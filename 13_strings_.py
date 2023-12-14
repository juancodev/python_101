text = 'Aprendiendo a programar en 1 simple paso con Python'
# print('JavaScript' in text)

lenguage = 'Python'

if lenguage in text:
  print('Sí está en el texto')
else:
  print('No, no está en el texto')

# length of text

sizeText = len(text)
print(sizeText)

# upper case
print(text.upper())

# lower case
print(text.lower())

# swap case
print(text.swapcase())

# title case
print(text.title())

# count letter
print(text.lower().count('a'))

# capitalize
print(text.capitalize())

# startWith
print(text.startswith('Aprendiendo'))

# endsWith
print(text.endswith('Python'))

# is a digit
text_2 = '123'
print(text_2.isdigit())

# replace
print(text_2.replace('123', 'Esto es un texto remplazado'))
