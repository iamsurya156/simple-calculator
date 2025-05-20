def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return " Error! Division by zero."
    return x / y

def print_menu():
    print("Welcome to the Calculator Human")
    print("Choose an operation:")
    print("  1️Add")
    print("  2  Subtract")
    print("  3️Multiply")
    print("  4️Divide")
    print("  5️Exit")

while True:
    print_menu()
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Thank you for using the calculator human, byeee")
        break

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid option. Please select from 1 to 5.")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
