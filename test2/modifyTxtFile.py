# Define the input and output file names
input_file = 'C:\\Users\\dillibabu.nsp\\Downloads\\20230727200135302.txt'
output_file = 'converted_output.txt'

# Open the input and output files
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Iterate through each line in the input file
    for line in infile:
        # Replace '*' with ',' and remove '~'
        new_line = line.replace('*', ',').replace('~', '')
        # Write the modified line to the output file
        outfile.write(new_line)

# Print a message when done
print("Conversion complete. Check the output in", output_file)
