import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count  = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count  = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count  = len(data[data["Primary Fur Color"] == "Black"])

print(f"Gray squirrels: {gray_squirrels_count}")
print(f"Red squirrels: {red_squirrels_count}")
print(f"Black squirrels: {black_squirrels_count}")

# two key value pairs
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
# create dataframe
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
