#tarea clase 6 febrero crear una listab de 5 números enteros
#list = [5,8,9,8,5]
"""
print(sum(list))
print(min(list))
print(max(list))
"""
"""list2 = []
num1 = int(input(f"Ingrese el primer número de la lista: "))
list2.append(num1)
num2 = int(input(f"Ingrese el primer número de la lista: "))
list2.append(num2)
num3 = int(input(f"Ingrese el primer número de la lista: "))
list2.append(num3)
num4 = int(input(f"Ingrese el primer número de la lista: "))
list2.append(num4)
num5 = int(input(f"Ingrese el primer número de la lista: "))
list2.append(num5)
print(list2)
suma = sum(list2)
print(f"La suma total de los números de la lista es ",suma)
print(f"El número mínimo de los números de la lista es ", min(list2))
print(f"El número máximo de la lista es ", max(list2))
#list2[0:2] = [10, 12]
valores = len(list2)

print(list2)
list2.sort()
print(f"Esta es la lista organizada de menor a mayor: ", list2)
thisset = set(list2)
print(thisset)
list3 = list(thisset)
list3.sort()
print(list3)
print(F"El segundo número más grande es: ", list3[1])
print(f"El número que es anterior al máximo es: ", list3[-2])
promedio = suma / valores
print(f"El promedio de los valores de la lista es: ", promedio)"""

# Ejercicio crear una lista de 5 palabras, encontrar longitud lista, la palabra más corta y larga y conectar dos palabras separadas por espacio.

list4 = []
palabra1 = input(f"Ingrese el primer número de la lista: ")
list4.append(palabra1)
palabra2 = input(f"Ingrese el primer número de la lista: ")
list4.append(palabra2)
palabra3 = input(f"Ingrese el primer número de la lista: ")
list4.append(palabra3)
palabra4 = input(f"Ingrese el primer número de la lista: ")
list4.append(palabra4)
palabra5 = input(f"Ingrese el primer número de la lista: ")
list4.append(palabra5)
print(list4)
largo = len(list4)
print(f"La longitud de la lista es: ", largo)
print(f"La palabra más corta de la lista es: ", min(list4, key = len))
print(f"La palabra más larga de la lista es: ", max(list4, key = len))

