### Functions ###

# Definición

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

# Función con parámetros de entrada/argumentos

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5,6)
sum_two_values(5433, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entradas/argumentos por clave

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Maldonado", name="Edu")

# Función con parámetros de entrada/argumentos por defecto

def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Edu","Maldonado")
print_name_with_default("Edu", "Maldonado", "MoureDev")

# Función con parámetros de entrada/argumentos arbitrarios

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")