# File paths
input_file = "day1_data.txt"        # your R32 format file
output_file = "day1_data_fixed.py"  # file to save the list of tuples

# Read input and convert to list of tuples
moves_list = []
with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if line:  # skip empty lines
            direction = line[0]        # first character
            value = int(line[1:])      # rest as integer
            moves_list.append((direction, value))

# Export the list to a file with one tuple per line
with open(output_file, "w") as f:
    f.write("moves = [\n")
    for move in moves_list:
        f.write(f"    {move},\n")  # 4-space indentation for readability
    f.write("]\n")
