import pandas

data = pandas.read_csv("weather_data.csv")

# print(data)
#
# print(data["temp"].mean())
#
# print(max(data["temp"]))

print(data[data.day == 'Tuesday'])
