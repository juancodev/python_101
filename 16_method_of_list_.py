numbers = [1, 2, 3, 4]

print(numbers[1])

numbers[-1] = 10

print(numbers)

# add new element to us list

numbers.append(11)

print(numbers)

# insert a new value from its position indicated

numbers.insert(0, 0)
print(numbers)

# merge or concat list

numbers2 = [12, 13, 14, 15]

newList = numbers + numbers2

print(newList)

# index of an element

indexOfAnElement = newList.index(13)
newList[indexOfAnElement] = 12.5

print(newList)

# delete an element specif

newList.remove(
  12.5
)  # if the element is not in the list, it will raise an error but the element be extacted

print(newList)

# pop the last element
newList.pop()

print(newList)

# pop with an index defined
newList.pop(0)

print(newList)

# reverse the list

newList.reverse()
print(newList)

# sort the list
newListUnOrder = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newListUnOrder.sort()
print(newListUnOrder)

newListUnOrder.insert(0, 'hi')
print(newListUnOrder)

newListUnOrder[13:] = 'hello'
print(newListUnOrder)