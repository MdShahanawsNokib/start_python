#Exercise 1: Area Of a rectangle
# 
lenght = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: ")) 
area = lenght * width
print(f"The area of the rectangle is : {area} cm sequer units")


#Exercise 2 : shopping cart program

item= input("What item do you want to buy? : ")
quantity = int(input("How many do you want to buy?: "))
price_pre_item= float(input("What is the price per item? : "))
total= quantity * price_pre_item

print(f"You ordered {quantity} {item}/s at {price_pre_item} each.")
print(f"Your total is: {total}")


