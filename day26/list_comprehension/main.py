import random

# consider creating a list from another list
# for example, if we have a list of numbers and want a new list of each item plus 1, we'd have to use a for loop
numbers = [1,2,3]
new_list = []
for i in numbers:
    new_list.append(i + 1)
print(new_list)  # [2,3,4]

new_list_comprehension = [x+1 for x in numbers]  # [new_item for item in list]
print(new_list_comprehension)  # [2,3,4]

# you can also iterate over things like strings
name = "Craig"
name_cap_letters = [letter.upper() for letter in name]
print(name_cap_letters)

# or ranges
nums = range(1,5)
doubles = [i * 2 for i in nums]
print(doubles)

# we can also use conditional statements in our list comprehensions
first10 = range(1,11)
evens = [x for x in first10 if x % 2 == 0]
print(evens)

# Challenge - Squaring numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squares = [i ** 2 for i in numbers]
print(squares)

# There are also dictionary comprehensions
# new_dict = {new_key:new_value for item in list if test}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
names = ['craig', 'john', 'charles', 'scott']
student_scores = {name : random.randint(50, 100) for name in names}
print(student_scores)

passed_students = {key : value for (key, value) in student_scores.items() if value >= 70}
print(passed_students)

# dict comprehension exercise 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# create a dict that includes the number of letters in each word
letters_per_word = {word : len(word) for word in sentence.split(" ")}
print(letters_per_word)

# dict comprehension exercise 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday":24,
}
# create a corresponding dict for weather with degrees in farenheight
weather_f = {day: temp * 9/5 + 32 for (day, temp) in weather_c.items()}
print(weather_f)

