from pathlib import Path

file_path = Path(__file__).resolve().parent / "2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260722.csv"
# with file_path.open("r") as file:
#     data = file.readlines()
#     print(data)

# import csv 

# with file_path.open("r") as file:
#     data=csv.reader(file)
#     tempurature=[]
#     for row in data:
#         if row[1] != "temp":
#             tempurature.append(row[1])
#     print(tempurature)

import pandas

# data = pandas.read_csv(file_path)
# list=data["temp"].to_list()
# print(list)
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# c=monday.temp
# f=float((c*1.8)+32)
# print(f)

data = pandas.read_csv(file_path)

# Access column name with spaces using bracket notation
black = data[data["Primary Fur Color"] == "Black"]
gray=data[data["Primary Fur Color"] == "Gray"]
cinnamon=data[data["Primary Fur Color"] == "Cinnamon"]
black_count=len(black)
gray_count=len(gray)
cinnamon_count=len(cinnamon)

data_dict={
"fur color":["Gray","Black","Cinnamon"],
"count":[gray_count,black_count,cinnamon_count]

}

df=pandas.DataFrame(data_dict)
df.to_csv("squirel_count.csv")
