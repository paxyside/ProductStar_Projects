filename = input("Enter filename: ")
try:
    with open(filename, 'r') as file:
        num_lines = len(file.readlines())
        print("Num of lines: ", num_lines)
except FileNotFoundError:
    print("File not found.")