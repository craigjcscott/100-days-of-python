# with open("weather_data.csv") as weather_file:
#     weather_data = weather_file.readlines()
#     print(weather_data)

##########

# import csv
#
# with open("weather_data.csv") as weather_file:
#     weather_data = csv.reader(weather_file)  # csv reader automatically splits, strips, and listifies
#     temps_list = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temps_list.append(int(row[1]))
#     print(temps_list)

##########

import pandas as pd

weather_data = pd.read_csv("weather_data.csv")
# print(f"weather data type: {type(weather_data)}")  # DataFrame, basically entire csv/table
# print(f"temp column type: {type(weather_data['temp'])}")  # Series, basically a list of a single column
# print(weather_data["temp"])

# weather_data_dict = weather_data.to_dict()   # creates a dict for each column
# print(weather_data_dict)

temp_list = weather_data["temp"].to_list()  # convert series to a list
print(temp_list)

# Find the mean temp
# mean_temp = sum(temp_list) / len(temp_list)
mean_temp = weather_data["temp"].mean()
print(f"mean temp = {mean_temp}")
max_temp = weather_data["temp"].max()
print(f"max temp = {max_temp}")

# Get data in a column
# print(weather_data["condition"])
print(weather_data.condition)  # Pandas converts the columns into attributes

# Get data in a row
print(weather_data[weather_data.day == "Monday"])

# Example: Which day had the highest temperature?
print(f"day with hottest temp: {weather_data[weather_data.temp == weather_data['temp'].max()]['day']}")

print(f"Monday C* temp: {round((int(weather_data[weather_data.day == 'Monday']['temp']) - 32) * 5/9,1)} C*")

# Create a data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")