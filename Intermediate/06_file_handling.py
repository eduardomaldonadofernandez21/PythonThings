### File Handling ###

import xml
import csv
import json
import os

# .txt file

# Leer, escribir y sobreescribir si ya existe


txt_file = open("Intermediate/my_file.txt", "w+") # Leer y escribir

txt_file.write(
    "Mi nombre es Edu\nMi apellido es Maldonado\n24 años\nY mi lenguaje preferido es Python")

#print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())

for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline())

txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

#os.remove("Intermediate/my_file.txt")

# .json file

json_file = open("Intermediate/my_file.json","w+")

json_test = {
    "name": "Edu",
    "surname": "Maldonado",
    "age": 24,
    "language": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev"
}

json.dump(json_test, json_file, indent=4)

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Edu", "Maldonado", "24", "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

csv_file.close()

with open('Intermediate/my_file.csv', "a",newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    csv_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open('Intermediate/employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
    
# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file
