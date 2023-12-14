text = 'Aprendiendo a programar en Python'
print(text)
print(text[0])
print(text[1])
# print(text[999])  => Error: IndexError: string index out of range

size = len(text)
print('size of text => ', size)
print(text[size - 1])
print(text[-1])
print(text[-2])

# Slicing

print(text[0:11])
print(text[0:23])
print(text[27:33])

# por lógica sabemos que el índice siempre será 0 se puede omitir

print(text[:11])

# viceversa

print(text[14:])

# print all

print(text[:])

# imprimir con salto de línea

print(text[27:33:1])
print(text[27:33:2])
print(text[::2])