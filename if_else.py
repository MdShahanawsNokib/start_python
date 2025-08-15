#fi_else Statement 

age = int(input("Enter your age: "))

if age >= 80:
    print("You are too old to sign up.")

elif 18 <= age < 80:
    print("You are eligible to sign up.")

elif age<=0:
    print("You are not born yet or you entered an invalid age.")

else:
    print("You are not aligible to sign up.")