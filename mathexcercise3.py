#Hypontenuse of a triangle 

import math

a= float(input("Enter the length of side a / hight:"));
b= float(input("Enter the lenght of side b/ base: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
result = round(c, 2)

print(f"The Hypotenuse of the triangle is: {result} cm")