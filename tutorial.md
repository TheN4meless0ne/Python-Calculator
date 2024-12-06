# How to make a calculator using Python.
In this tutorial we will learn how to make a calculator that asks the user what sort of equation they want to have solved. To do this we will be taking use of a few different python functions and statements including the `if` statements, and the `input()` and `lambda` functions, as well as making a few functions of our own.

# Part 1 - Making the main program
## Step 1
The first step towards a working calculator is setting up the part of the program that asks the user what they would like to do. This can be done using the `input()` function in python, and by having the value of a python variable set to the output of said function.

```py
userChoice = input("How would you like to calculate? (add, subtract, multiply, divide): ").lower()
```

You'll notice that I have written `.lower()` at the end of my function. This makes it so that the user can write their answer with any amount of capitalisation they might want without having it break. If your program is dependent on an answer to function, this is the best way to make sure it doesn't break by e.g. accidentally having caps lock switched on.

## Step 2
After we've established the value of the variable `userChoice`, and how to set its value, we need to use it. This is where our `if` statements come in handy. We can use an if statement to have something happen if `userChoice` is holding a certain string.

We will be setting up our `if` statement in a way where it calls for some functions, which we will soon create, to be used. As of right now, however, your calculator will not work,

```py
if userChoice == "add":
    add(num1, num2)
elif userChoice == "subtract":
    subtract(num1, num2)
elif userChoice == "multiply":
    multiply(num1, num2)
elif userChoice == "divide":
    divide(num1, num2)
```

Our if statements call for 1 function each and using two variables, `num1` and `num2`. If the user was to type in "add", a function named `add` would be called and would execute the code of the function, adding the values of `num1` and `num2` and printing the answer.

## Step 3
Now it is time to connect our two pieces of code. However, before we do this, I want to call for another function. This function will be used to get the values of `num1` and of `num2` allowing our functions to run.

```py
num1, num2 = getNumbers()
```

We want to add this function right under our user input and above our `if` statements.

Our code should look like the following after completing step 3.

```py
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
```

## Step 4
Before we can proceed to adding functionality to our calculator, we need to place our program inside a `while` loop. This will make it so that our code loops until we tell it to stop, which we can do by writing `break` at the point we want to stop at.

```py
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
```

You'll notice that I've done a little more than just add `while True:` to our code. I have also gone ahead and added a comment on the top, symbolised by the "#", a `print()` giving us a nice welcome message, an `else` statement giving us a little error message if we were to type anything other than our four options and then uses a tag called `continue` to send us back to the top of the loop, making it repeat until we enter one of our predetermined answers, and lastly, I've added `break` to the end of our loop, stopping the cycle. If you want the program to start over after it has solved your equation, you can do this by removing `break` from the loop.

# Part 2 - Functions and Variables
## Step 1
Now that we have built our main program it is time to add som functionality to it. To do this we firstly need a way to set a value to `num1` and `num2`. To do this we will need to build the `getNumbers()` function that we added to our main program in part 1.

```py
def getNumbers():
    num1 = getNumber("Enter first number: ")
    num2 = getNumber("Enter second number: ")
    return num1, num2
```

The `getNumbers()` function isn't very big, and you'll notice it uses yet another function called `getNumber()` to set the value of `num1` and `num2`. <br>
`getNumber()` uses a `prompt`, a predetermined string in an input to get the value of our two main variables, `num1` and `num2`. This is done in order to repeat as little code as possible, allowing us to add more numbers to our equations without having to do too much work.

```py
def getNumber(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
```

You'll notice that I am using `try` and `except ValueError` inside a `while` loop. This tells the code to try to return a `float`, a number with decimals, except when the user enters a value that is not numerical. If the number is not numerical, the program will let you know with a `print()` and allow you to enter a new value for your number.

## Step 2
Believe it or not, but the only thing left to do in our calculator program is to have it do the math. We can do this using a few `lambda` functions. A `labda` function allows you to have your function happen on a single line of code. We can use `lambda` functions for three of our equations, as they don't have any exceptions on what you can enter without crashing our program.

```py
add = lambda num1, num2: print(num1 + num2)
subtract = lambda num1, num2: print(num1 - num2)
multiply = lambda num1, num2: print(num1 * num2)
```

Our function for division does unfortunately need to be a little longer, as your python program will break if you divide by 0. This means that we have to make an exception if the user enters 0 as the value of `num2` letting them know that they can't do that and allowing them to give `num2` a new value.

```py
def divide(num1, num2):
    while num2 == 0:
        print("Cannot divide by zero. Please enter a new number.")
        num2 = getNumber("Enter second number: ")
    print(num1 / num2)
```

This `while` loop will only activate if the user enters 0 as the value of `num2` after selecting division. If this doesn't happen, it will do the same thing as the other functions and print out the result of the equation.

# Part 3 - It's all coming together now
After you've made your functions it is important to know that when we're writing code, we place our variables and functions in the order that they are used. The code that is used the most is the code that should be at the top.

This is how our final code should look:

```py
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
```

In ourcase, we would want to place the `getNumber()` function at the top of our program as it is not dependant on any other function, but rather being depended on. Just after comes `getNumbers()`, being the only function (except `divide()`) that calls for `getNumber()` it is only natural to have it placed right beneath the function it calls. Then we would want to define our functions for equation, in the order they are called as that is the easiest way to find them later on if you should need to change anything. And finally our main program. The main program comes last, as it depends on all functions above it to work.

With how good todays technology has gotten, you most likely won't face any large issues if you mess up the order of which you place your functions and variables. However, it having a good order in your project does make it easier to read, and thus makes it easier to help or to grade if that should be needed.