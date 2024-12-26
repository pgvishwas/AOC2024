from itertools import product
def productVal(num):
    prod =1
    for i in num:
        prod*=i
    return prod

def checkValidity(num, values):
    numVar = []
    valuesVar = []
    for i in range(len(num)):
        if  not (num[i] < sum(values[i]) or num[i] > productVal(values[i])):
            numVar.append(num[i])
            valuesVar.append(values[i])
    return numVar,valuesVar


def caliberation(num,values):
    bridgeArr = 0
    for i in range (len(num)):
        equations = generate_equations(values[i])
        for eq in equations:
            result = evaluate_left_to_right(eq)
            if result == num[i]:
                bridgeArr+=result
                break
    return bridgeArr

def evaluate_left_to_right(equation):
    # Split the equation into tokens (numbers and operators)
    tokens = equation.replace('+', ' + ').replace('*', ' * ').replace('|',' | ').split()

    # Convert numbers to integers
    parsed_tokens = [int(token) if token.isdigit() else token for token in tokens]

    # Evaluate the equation left-to-right
    result = parsed_tokens[0]  # Start with the first number
    i = 1  # Start at the first operator

    while i < len(parsed_tokens):
        operator = parsed_tokens[i]
        operand = parsed_tokens[i + 1]

        # Perform the operation
        if operator == '+':
            result += operand
        elif operator == '*':
            result *= operand
        elif operator == '|':
            result = int(f"{result}{operand}")

        # Move to the next operator
        i += 2

    return result


def generate_equations(numbers):
    # All possible operators
    operators = ['+', '*','|']

    # Generate all possible combinations of operators
    operator_combinations = product(operators, repeat=len(numbers) - 1)

    # Create equations
    equations = []
    for combo in operator_combinations:
        equation = ""
        for i, num in enumerate(numbers):
            equation += str(num)  # Add the current number
            if i < len(combo):  # Add the corresponding operator if it exists
                equation += combo[i]
        equations.append(equation)

    return equations




with open("../input_day7.txt", "r") as file:
    input_data = file.readlines()
num = []
values = []

for item in input_data:
    # Split the string on ':'
    parts = item.split(':')

    # Extract the first number and convert it to integer
    num.append(int(parts[0].strip()))

    # Extract the rest of the numbers, split by space, and convert to a list of integers
    values.append(list(map(int, parts[1].strip().split())))

#num,values = checkValidity(num,values)
caliberArr = caliberation(num,values)
print(caliberArr)