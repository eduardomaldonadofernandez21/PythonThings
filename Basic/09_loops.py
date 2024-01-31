### Loops ###

# While

my_condiction = 0

while my_condiction < 10:
    print(my_condiction)
    my_condiction += 2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condiction < 20:
    my_condiction += 1
    if my_condiction == 15:
        print("Se detiene la ejecución")
        break
    print(my_condiction)

print("La ejecución continua")

# For

my_list = [35, 25, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Edu", "Maldonado", "Edu")

for element in my_tuple:
    print(element)

my_set = {"Edu", "Maldonado", 23}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continua")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")