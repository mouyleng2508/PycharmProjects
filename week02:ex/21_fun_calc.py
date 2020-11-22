def fun_calc(num1, num2, operator):
    if operator == "+":
        results = num1 + num2
        return f"Product: {results}\nProcess: {num1} + {num2} = {results}"
    elif operator == "-":
        results = num1 - num2
        return f"Product: {results}\nProcess: {num1} - {num2} = {results}"
    elif operator == "*":
        results = num1 * num2
        return f"Product: {results}\nProcess: {num1} * {num2} = {results}"
    elif operator == "/":
        results = num1 / num2
        return f"Product: {results}\nProcess: {num1} / {num2} = {results}"

results = 0
calculate = fun_calc(50, 2, "*")
print(calculate)
