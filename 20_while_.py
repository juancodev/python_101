'''
  while condiction == True:
    iterator for change the condiction
    ...logic
'''

# while loop
print('While loop')

counter = 0

while counter < 10:
  counter += 1
  print(counter)

# while with break
print('While with break')

counter = 0

while counter < 20:
  counter += 1
  if counter == 15:
    break
  print(counter)

# while with continue
print('While with continue')

counter = 0

while counter < 20:
  counter += 1
  if counter < 15:
    continue
  print(counter)