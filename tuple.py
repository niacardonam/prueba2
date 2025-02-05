""" 
Las tuples son ordenadas, el orden no cambia, permiten valores duplicados, despues de creada no se le pueden añadir, remover o cambiar elementos

Ejercicio Profesor
tuple1 = ("banana", "apple", "cherry")
tuple2 = (15, "masa", (59,14,"hola",False), 3.1416, True, ["Mazada", "Renault", "Fiat"],15)
print((tuple2[1][0]))
print(tuple2[1])

frutas = ("fresa", "papaya", "mango", "papaya")
print(frutas.count("papaya"))
print(frutas.index("papaya"))
copia = list(frutas)
print(frutas)
print(copia)
copia.append("mango")
print(copia)
frutas = tuple(copia)
print(frutas)"""

#ejercicio tuples
mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(len(mytuple))
mytuple2 = ("apple", "banana", "cherry", "apple")
print(mytuple2)
print(len(mytuple2))
#Tuple con un elemento debe tener una coma(,) después de enunciarlo porque si no, es una variable y no una tuple con una variable
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tipos de datos en las tuples

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

#Una tuple contiene diferentes tipos de datos
tuple4 = ("abc", 34, True, 40, "male")
print(tuple4)
thistuple3 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple3)

          