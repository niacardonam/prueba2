"""no es ordenado"""
"""no tiene elementoas repetidos o duplicados"""
"""conjunto = {58, "carro", 3.1416, True }
print(conjunto)
conjunto.add("florecita")
print(conjunto)
conjunto2 = conjunto.copy()
print(conjunto2)"""
"""frutas1 = {"papaya", "mango", "fresa", "mora"}
frutas2 = {"mango", "mora"}
print(frutas1.difference(frutas2))
print(frutas1.intersection(frutas2))
print(frutas2.issubset(frutas1))
print(frutas1.issuperset(frutas2))
print(frutas1.pop())
frutas1.remove("papaya")
print(frutas1)"""

#Ejercicios web
myset = {"apple", "banana", "cherry"}
#los conjuntos no tienen orden, los elemntos no tiene un orden definido, no tienen indexación (las variables o elementos no estan fijas), no cambia el conjunto pero se pueden adicionar o eliminar elementos.
print(myset)
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# True y 1 es asumido como el mismo valor
thisset1 = {"apple", "banana", "cherry", True, 1, 2}

print(thisset1)

# False y 0 es asumido cmo el mismo valor
thisset2 = {"apple", "banana", "cherry", False, True, 0}

print(thisset2)

# obtener el tamaño del conjunto o número de elementos
thisset3 = {"apple", "banana", "cherry"}

print(len(thisset3))

# TIPOS DE DATOS EN CONJUNTOS

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

# pemite varios tipos de datos
set4 = {"abc", 34, True, 40, "male"}

print(set4)
print(type(set4))

thisset5 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset5)