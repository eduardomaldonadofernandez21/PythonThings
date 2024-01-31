### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for i in range(101):
        if i % 5 == 0 and i % 3 == 0:
            print("fizzbuzz\n")
        elif i % 5 == 0:
            print("buzz\n")
        elif i % 3 == 0:
            print("fizz\n")
        else:
            print(f"{i}\n")

#fizzbuzz()


"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    if len(word_one) != len(word_two):
        return False
    for char in word_one.lower():
        if(word_two.lower().count(char) == 0):
            return False
    return True

def is_other_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram("Amor", "Roma"))


"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    x, y = 0,1
    for i in range(1,51):
        fib = x+y
        x,y = fib, x
        print(x)
    return x

#fibonacci()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
def is_prime():
    list_primes = []
    for prime in range(2, 100):
        for i in range(1,prime+1):
            if(i == prime):
                list_primes.append(prime)
            elif(prime % i == 0 and i != 1):
                break
    print(list_primes)

#is_prime()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(text):
    newText = ""
    for i in range(len(text)):
        newText += text[len(text) - i -1] 
    return newText

print(reverse("Hola mundo"))
