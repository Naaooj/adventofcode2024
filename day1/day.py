import os

# Initialize two empty lists to store the columns
left = []
right = []

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the input file
file_path = os.path.join(script_dir, 'input.txt')

# Open the file and read it line by line
with open(file_path, 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        left.append(num1)
        right.append(num2)

# Sort the lists in ascending order
left.sort()
right.sort()

total_distance = sum(abs(l - r) for l, r in zip(left, right))

print("total distance", total_distance)