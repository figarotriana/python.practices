while True:
    user_input = input("Enter an operation (e.g., 2-4): ")
    for operator in "+-*/":
        if operator in user_input:
            parts = user_input.split(operator)
            try:
                num1 = float(parts[0])
                num2 = float(parts[1])
                if operator == "+":
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "*":
                    result = num1 * num2
                elif operator == "/":
                    result = num1 / num2
                print("Result:", result)
            except ValueError:
                print("Please enter valid numbers!")
            break
