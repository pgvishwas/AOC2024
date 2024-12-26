import re

def string_to_multiplication(expression):
    # Regular expression to extract the numbers inside "mul(a,b)"
    pattern = r"mul\((\d+(?:\.\d+)?),(\d+(?:\.\d+)?)\)"
    match = re.match(pattern, expression)

    if match:
        # Extract the two numbers
        a = float(match.group(1))  # Convert first number to float
        b = float(match.group(2))  # Convert second number to float
        # Return the result of multiplication
        return a * b
    else:
        raise ValueError("Invalid input format. Expected 'mul(a,b)' with a and b as numbers.")

def checkMul(a):
    textVal = a
    pattern = r"mul\(\d+(?:\.\d+)?,\d+(?:\.\d+)?\)"
    resultVal = re.findall(pattern,textVal)
    return resultVal
with open("../input_day3.txt", "r") as file:
  input_data = file.readlines()
res = "".join(input_data)
result = checkMul(res)
sumVal =0
for i in result:
    sumVal += string_to_multiplication(i)

print(sumVal)
