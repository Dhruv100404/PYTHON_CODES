import requests
from datetime import datetime
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# print(response.status_code)
#

parameters = {
    "lat": 23.215635,
    "lng": 72.636940,
    "formatted":0,
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
time = datetime.now()
sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
print(time.hour)