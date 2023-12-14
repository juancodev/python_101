name = "Juan"
last_name = "Montilla Sanchez"
age = "24"
username = "juancodev"

template = "Mi nombre es " + name + " y mi apellido es " + last_name + " y tengo " + age + " y me pueden seguir en mis redes sociales como: " + username

print('V1 =>', template)

template = "Mi nombre es {} y mi apellido es {}, tengo {} y me pueden seguir en mis redes sociales como: {}".format(
  name, last_name, age, username)

print('v2 =>', template)

template = f'Mi nombre es {name} y mi apellido es {last_name}, tengo {age} y me pueden seguir en mis redes sociales como: {username}'

print('v3 =>', template)