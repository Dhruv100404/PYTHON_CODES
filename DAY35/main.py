import requests
api_key = "ca6c32e487f9b623261018492c95de4b"
parameters = {



}

response = requests.get("https://api.openweathermap.org/data/2.5/weather" , params=parameters)
