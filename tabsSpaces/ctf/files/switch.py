def switch_spaces_and_tabs(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r') as infile:
        content = infile.read()  # Read the content of the file

    # Replace spaces with 'a' and tabs with 'b'
    modified_content = content.replace(' ', '0').replace('\t', '1')

    # Open the output file for writing
    with open(output_file, 'w') as outfile:
        outfile.write(modified_content)  # Write the modified content to the output file

    print(f"File '{input_file}' processed and saved as '{output_file}'.")

# Example Usage
input_filename = 'whitespace_flag.txt'  # Replace with the input file name
output_filename = 'output.txt'  # Replace with the desired output file name

switch_spaces_and_tabs(input_filename, output_filename)
