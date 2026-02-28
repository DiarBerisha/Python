
def challenge(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    else:
        raise ValueError("Invalid operation.")


try:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    op = input("Enter an operation (+, -, *, /): ")


    result = challenge(num1, num2, op)


    print("Result:", result)

except ValueError as ve:
    print("ValueError:", ve)

except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Program has ended.")

