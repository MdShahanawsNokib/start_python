#convert kg to pound and  pound to kg

unit = input("Enter the unit to convert (kg or pound): ")

if unit == "kg": 
    kg = float(input("Enter weight in kg: "))
    pound = kg * 2.20462;
    print(f"{kg} kg is equal to {pound} pounds")
elif unit == "pound":
    pound = float(input("Enter weight in pounds: "))
    kg =pound/2.20462
    print(f"{pound} pound is qual to {kg} kg");
else:
    print("Invalid unit. Please enter 'kg' or 'pound'.")

    


