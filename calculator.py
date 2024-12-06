# Functions to get numbers for equation
def getNumber(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def getNumbers():
    num1 = getNumber("Enter first number: ")
    num2 = getNumber("Enter second number: ")
    return num1, num2

# Functions for calculations
add = lambda num1, num2: print(num1 + num2)
subtract = lambda num1, num2: print(num1 - num2)
multiply = lambda num1, num2: print(num1 * num2)

# Divide function needs to check for division by zero
def divide(num1, num2):
    while num2 == 0:
        print("Cannot divide by zero. Please enter a new number.")
        num2 = getNumber("Enter second number: ")
    print(num1 / num2)

# Main program
print("Welcome to the calculator!")
while True:
    userChoice = input("How would you like to calculate? (add, subtract, multiply, divide): ").lower()
    num1, num2 = getNumbers()
    if userChoice == "add":
        add(num1, num2)
    elif userChoice == "subtract":
        subtract(num1, num2)
    elif userChoice == "multiply":
        multiply(num1, num2)
    elif userChoice == "divide":
        divide(num1, num2)
    else:
        print("Invalid input. Please try again.")
        continue
    break