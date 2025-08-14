# Circumference of a circle

import math

r = float(input("Enter the radius of the circle: "))

circumference = 2* math.pi * r;
result = round(circumference, 2)

print(f"The circumference of the circle is: {result} cm")

