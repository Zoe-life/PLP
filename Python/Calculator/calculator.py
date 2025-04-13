def calculate(num1, num2, operation):
    """
    Performs a mathematical operation based on the given inputs.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform (+, -, *, /).

    Returns:
        float: The result of the operation.  Returns None if the operation is invalid
               or if division by zero is attempted.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        print("Error: Division by zero is not allowed.")
        return None
    else:
        print("Error: Invalid operation. Please use +, -, *, or /.")
        return None



def get_user_input():
    """
    Gets the two numbers and the operation from the user, handling potential errors.

    Returns:
        tuple: (num1, num2, operation) if input is valid, (None, None, None) otherwise.
    """
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    operation = input("Enter the operation (+, -, *, /): ")
    return num1, num2, operation



def main():
    """
    Main function to run the calculator program.
    """
    print("Welcome to the Simple Calculator!")

    num1, num2, operation = get_user_input()  # Get input and handle errors

    if num1 is None or num2 is None or operation is None:
        print("Terminating Program")
        return

    result = calculate(num1, num2, operation)  # Perform the calculation

    if result is not None:
        print(f"{num1} {operation} {num2} = {result}")



if __name__ == "__main__":
    main()