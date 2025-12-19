import pandas
from pandas import value_counts

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#returns index name , value/counts
color_count = data["Primary Fur Color"].value_counts()

df = pandas.DataFrame({"Fur Color" : color_count.index, "Count" : color_count.values})

df.to_csv("squirrel_count.csv")




