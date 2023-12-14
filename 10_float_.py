x = 3.3
print(x)

y = 1.1 + 2.2
print(y)

print(x == y)

# first form with format

float_str = format(y, '.2g')
print(float_str)
print(x == float(float_str))

print('*' * 10)

x = 3.3
print(x)

y = 1.1 + 2.2
print(y)

print(x - y)

print(abs(x - y) < 0.001)
