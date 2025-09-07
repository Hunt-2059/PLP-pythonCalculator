# Hunt-2059
# For now this is a simple calculator that can handle two or three inputs.
# It can add, subtract, multiply, and divide the numbers.
print("For now this is a simple calculator that can handle two or three inputs.")
print("It can add, subtract, multiply, and divide the numbers.")
def calculator():
    answer = str(input("How many inputs do you want to enter? (2 or 3): "))
    if answer == "2":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operation = str(input("Enter the operation (+, -, *, /): "))
        if operation == "+":
            print(f"The result is: {a + b}")
        elif operation == "-":
            print (f"The result is: {a - b}")
        elif operation == "*":
            print (f"The result is: {a * b}")
        elif operation == "/":
            print (f"The result is: {a / b}")
        else:
            print("Invalid operation")
    elif answer == "3":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        c = float(input("Enter the third number: "))
        operation = str(input("Enter the operation (+, -, *, /): "))
        if operation == "+":
            print(f"The result is: {a + b + c}")
        elif operation == "-":
            print (f"The result is: {a - b - c}")
        elif operation == "*":
            print (f"The result is: {a * b * c}")
        elif operation == "/":
            print (f"The result is: {a / b / c}")
        else:
            print("Invalid operation")
calculator()