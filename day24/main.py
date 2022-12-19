# with open("my_file.txt") as file:  # mode is set to r by default (read-only)
#     contents = file.read()  # returns contents as a string
#     print(contents)
# file.close()  # why close? it takes up resources. we close when done to avoid python closing it for us later
# not needed since we use with instead of assigning the open file to a variable

with open("new_file.txt", mode="a") as file:  # w = write, a = append
    file.write("\nThis is a new file.")  # overwrites existing text if using write, use append to add instead
# if you open a file in write mode, but the file doesn't exist, python creates the file for you.
