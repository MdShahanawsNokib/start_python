#area of a circle 
import math

r =float(input("Enter the radius of the circle: "))

area = r**2 * math.pi
result= round(area, 2)

print(f"The area of the circle is: {result} cm²")