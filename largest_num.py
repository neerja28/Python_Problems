num1 = int (input("Enter a number1: "))
num2 = int (input("Enter a number2: "))
num3 = int (input("Enter a number3: "))

if (num1 >= num2 and num1 >= num3):
    print (f"Number {num1} is greater")
elif (num2 >= num1 and num2 >= num3):
    print (f"Number {num2} is greater")
else:
    print (f"Number {num3} is greater")
