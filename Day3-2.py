import re


def calculate_enabled_multiplications(memory):
    # Regex patterns for do(), don't(), and mul(a,b)
    instructions_pattern = r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)"

    # Initialize state and total
    mul_enabled = True
    total_sum = 0

    # Find all instructions
    instructions = re.finditer(instructions_pattern, memory)

    for match in instructions:
        instruction = match.group(0)

        if instruction == "do()":
            mul_enabled = True
        elif instruction == "don't()":
            mul_enabled = False
        elif instruction.startswith("mul(") and mul_enabled:
            # Extract numbers a and b
            a, b = int(match.group(1)), int(match.group(2))
            # Add their product to the total sum
            total_sum += a * b

    return total_sum


# read input_data from file
with open("../input_day3.txt", "r") as file:
  input_data = file.readlines()
res = "".join(input_data)
print(calculate_enabled_multiplications(res))