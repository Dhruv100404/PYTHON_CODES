import pandas
import pandas as pd

data = pd.read_csv("squirrel.csv")

count1 = len(data[data["Primary Fur Color"] == "Gray"])
count2 = len(data[data["Primary Fur Color"] == "Cinnamon"])
count3 = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {

    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [count1, count2, count3]
}


df = pandas.DataFrame(data_dict)

df.to_csv("squirrel_count.csv")

