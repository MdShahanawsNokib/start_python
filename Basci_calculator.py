#Basic Calculator by Python

operator = input("Enter operator (+, -, *, /):")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator=="+": 
    result = num1+ num2
    print(f"The result is: {result}")

elif operator=="-": 
    result = num1 - num2
    print(f"The result is: {result}")

elif operator=="*": 
    result = num1 * num2
    print(f"The result is: {result}")

elif operator== "/" : 
    result = num1 / num2
    print(f"The result is: {result}")
else: 
    print("invalid operator, Please enter a valid operator (+,-,*,/)")