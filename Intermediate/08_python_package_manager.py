
### Python Package Manager ###

# PIP https//pypi.org

# pip install pip
# pip --version

# pip install numpy
import pandas
from mypackage import arithmetic
import numpy
import requests

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package

print(arithmetic.sum_two_values(1, 5))