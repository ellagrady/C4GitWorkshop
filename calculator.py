# calculator application
# make edits if you want, really just a filler file

# return sum of two numbers
def add(x, y):
    return x + y

# return difference of two numbers
def subtract(x, y):
    return x - y

# return product of two numbers
def multiply(x, y):
    return x * y

# return quotient of two numbers
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

if __name__ == "__main__":
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # numerical choice of operation
    choice = input("Enter choice(1/2/3/4): ")

    # take input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # calculate operation and print output
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")