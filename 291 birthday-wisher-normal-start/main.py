import random
import smtplib
from datetime import datetime

import pandas

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"

    with open("letter_1.txt") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        # print(contents)

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        # connection.starttls()
        connection.login("21ceuos020@ddu.ac.in", "Dhruv@104")
        connection.sendmail(
            from_addr="21ceuos020@ddu.ac.in",
            to_addrs=birthday_person["dhruvthakkar104@gmail.com"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
