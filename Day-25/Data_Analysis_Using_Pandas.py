
"""
with open("weather_data.csv") as data_file:
    data_set = data.readlines()
    print(data_set)
"""

# So many complications to use the csv file
"""
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []

    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)
"""

# This is the most useful way to read the csv file
"""
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
data_dict = data.to_dict()
print(data_dict)
data_list = data["temp"].to_list()
data = sum(data_list)/len(data_list)
print(data_list)

print(data["temp"].max())

          # Get data in column(You can use any of them)
print(data["condition"])
print(data.condition)

          # Get data in single row
print(data[data.day == "Monday"])
          Print the row of the maximum temp
print(data[data.temp == data["temp"].max()])

          # Create a dataframe from scratch
data_dict = {
    "students" : ["Amy", "Angela", "James"],
    "scores" : [55, 77, 66]
}
data_file = pandas.DataFrame(data_dict)
print(data_file)
data_file.to_csv("new_data.csv")

"""

# Analysing the data set of squirrel
import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count,black_squirrel_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")
