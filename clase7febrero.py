#Condicional
"""edad = 19
if edad >= 18:
    print(f"You area of legal age")
else:
    print(f"Your are a minor")
print("this way the flow continues")
"""
#several conditions
"""edad = 12

if edad > 0 and edad < 6:
    print("You are from early childhood")
elif edad >= 6 and edad < 13:
    print("chYou are an infant")
elif edad >= 13 and edad < 18:
    print("You are an adolecent")
else:
    print("You are an adult")
print("this way the flow continues")"""
#Exercise

"""num = int(input("Hello, please type a number: "))
print(f"Your number is: ", num)

if num < 0:
    print("The number is negative")
elif num == 0:
    print("The number is zero")
else:
    print("The number is positive")"""
# Exercise 2 triangle

print("Hello, please type the measures of the sides of triangle ")
side1 = float(input("Hello, please type a measure 1: "))
side2 = float(input("Hello, please type a measure 2: "))
side3 = float(input("Hello, please type a measure 3: "))

if side1 == side2 and side2 == side3:
    print("This is a equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("This is isosceles triangle")
elif side1 != side2 and side2!=side3:
    print("This is a scalene triangle" )
    

