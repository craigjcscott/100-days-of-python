# consider creating a list from another list
# for example, if we have a list of numbers and want a new list of each item plus 1, we'd have to use a for loop
numbers = [1,2,3]
new_list = []
for i in numbers:
    new_list.append(i + 1)
print(new_list)  # [2,3,4]

new_list_comprehension = [x+1 for x in numbers]  # [new_item for item in list]
print(new_list_comprehension)  # [2,3,4]
