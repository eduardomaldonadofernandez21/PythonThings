### Tuples ###

# Definición
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Edu", "Maldonado", "Edu")
my_other_tuple = (36, 60, 30)

print(my_tuple)
print(my_other_tuple)

# Acceso a elementos y búsqueda
print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Edu"))
print(my_tuple.index("Maldonado"))
print(my_tuple.index("Edu"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas

print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación
# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined