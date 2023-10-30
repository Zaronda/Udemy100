#with open("weather_data.csv") as data_file: 
#   data = data_file.readlines()
#    print(data)

#import csv
#with open("weather_data.csv") as data_file: 
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        # remove headings
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")
#print(data.tail(2))
#print(data)
#print(data["temp"])
#print(type(data))
data_dict = data.to_dict()
#print(data_dict)
#print(data["temp"].mean())
#print(data.condition)

# get data in rows
print(data[data.day == "Monday"])

# print max temp day
max_temp = data["temp"].max()
print(data[data.temp == max_temp])
# or 
print(data[data.temp == data.temp.max()])

# create dataframe from scratch
data_dict = {
    "students": ["Amy", "Brian", "Sue"],
    "scores": [76, 56, 64]
}
data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
