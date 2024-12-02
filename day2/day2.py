import os

def is_valid_sequence(sequence):
    if len(sequence) < 2:
        return False

    increasing = all(sequence[i] < sequence[i + 1] and 1 <= sequence[i + 1] - sequence[i] <= 3 for i in range(len(sequence) - 1))
    decreasing = all(sequence[i] > sequence[i + 1] and 1 <= sequence[i] - sequence[i + 1] <= 3 for i in range(len(sequence) - 1))

    print(increasing, decreasing)

    return increasing or decreasing

def filter_sequences(input_file):
    with open(input_file, 'r') as infile:
        nbrOfValidSequence = 0;
        for line in infile:
            sequence = list(map(int, line.split()))
            if (is_valid_sequence(sequence)):
                nbrOfValidSequence += 1
            
        return nbrOfValidSequence

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the input file
file_path = os.path.join(script_dir, 'input.txt')

print('Valid sequences', filter_sequences(file_path))