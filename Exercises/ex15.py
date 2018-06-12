from sys import argv

# assigns command line arguments to variables
script, filename = argv

# opens the file specified in the command line argument
txt = open(filename)

# opens, reads, and prints the specified file after printing the
# filename
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

# repeats the process above using input() as opposed to argv
print("Type the filename again:")
file_again = input("> ")

# opens file provided by the user through the input() above
txt_again = open(file_again)

# opens, reads, and prints the specified file
print(txt_again.read())
txt_again.close()
