import os

def is_valid_sequence(sequence):
    def check_sequence(seq):
        if len(seq) < 2:
            return False
        increasing = all(seq[i] < seq[i + 1] and 1 <= seq[i + 1] - seq[i] <= 3 for i in range(len(seq) - 1))
        decreasing = all(seq[i] > seq[i + 1] and 1 <= seq[i] - seq[i + 1] <= 3 for i in range(len(seq) - 1))
        return increasing or decreasing

    # Check if the sequence is valid as in part 1
    if check_sequence(sequence):
        return True

    # Check if the sequence is valid as in part 2
    for i in range(len(sequence)):
        # Remove the i-th element from the sequence and check if the new sequence is valid
        if check_sequence(sequence[:i] + sequence[i+1:]):
            return True

    return False

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