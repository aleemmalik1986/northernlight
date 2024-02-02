def compare_files(input_file1, input_file2, output_file1, output_file2):
    # Read the content of the first file
    with open(input_file1, 'r') as file1:
        file1_lines = set(file1.readlines())

    # Read the content of the second file
    with open(input_file2, 'r') as file2:
        file2_lines = set(file2.readlines())

    # Find lines unique to file1
    unique_to_file1 = file1_lines - file2_lines

    # Find lines unique to file2
    unique_to_file2 = file2_lines - file1_lines

    # Write the unique lines to the respective output files
    with open(output_file1, 'w') as outfile1:
        for line in sorted(unique_to_file1):
            outfile1.write(line)

    with open(output_file2, 'w') as outfile2:
        for line in sorted(unique_to_file2):
            outfile2.write(line)

# Example usage
input_file1 = './input1.txt'
input_file2 = './input2.txt'
output_file1 = './processfiles1_output1.txt'
output_file2 = './processfiles1_output2.txt'

# The function call would be
compare_files(input_file1, input_file2, output_file1, output_file2)
