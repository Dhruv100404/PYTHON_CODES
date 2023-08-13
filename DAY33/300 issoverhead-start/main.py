# import requests
# from datetime import datetime
#
# MY_LAT = 51.507351  # Your latitude
# MY_LONG = -0.127758  # Your longitude
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
#
# iss_latitude = float(data["iss_position"]["latitude"])
# iss_longitude = float(data["iss_position"]["longitude"])
#
# # Your position is within +5 or -5 degrees of the ISS position.
#
#
# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0,
# }
#
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
# time_now = datetime.now().hour
#
#
# def check():
#     if MY_LAT + 5 <= iss_latitude <= MY_LAT - 5 and MY_LONG + 5 <= iss_longitude <= MY_LONG - 5:
#
#         if sunset <= time_now <= sunrise:
#             import smtplib
#             s = smtplib.SMTP('smtp.gmail.com', 587)
#
#             s.starttls()
#
#             s.login("21ceuos020@ddu.ac.in", "Dhruv@104")
#
#             message = "Subject:Lookup\n\n The ISS is above you in the sky"
#
#             s.sendmail("21ceuos020@ddu.ac.in", "dhruvthakkar104@gmail.com", message)
#
#             s.quit()
#
#
# check()
import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:

    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )


