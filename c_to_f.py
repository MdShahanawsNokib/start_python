#Celsius ot Fahrenheit conversion

unit = input("Enter the unit to convert(c or f): ");

if unit == "c":
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32;
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif unit =="f":
    fahrenheit = float(input("Ente temperature in fahrenheit: "))
    celsius = (fahrenheit -32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid unit. Please enter 'c' or 'f'.") 