with open("Input/Letters/starting_letter.txt") as starting_file:
    starting_letter = starting_file.read()

with open("Input/Names/invited_names.txt") as names_file:
    list_of_names = names_file.read().split("\n")
    # could also use names_file.readlines() and the .strip() method to remove the \n

for name in list_of_names:
    named_letter = starting_letter.replace("[name]", name)
    file_name = f"Output/ReadyToSend/invite_for_{name}.txt"
    with open(file_name, "w") as invite_file:
        invite_file.write(named_letter)