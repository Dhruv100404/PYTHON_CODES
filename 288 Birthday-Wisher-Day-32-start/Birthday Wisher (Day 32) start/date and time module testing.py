import datetime as dt
import random

current = dt.datetime.now()

num = current.weekday()

if num == 6:

    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quotes = random.choice(all_quotes)


    import smtplib

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("21ceuos020@ddu.ac.in", "Dhruv@104")

    # message to be sent
    message = f"Subject:Satudray Motivation \n\n {quotes}"

    # sending the mail
    s.sendmail("21ceuos020@ddu.ac.in", "dhruvthakkar104@gmail.com", message)

    # terminating the session
    s.quit()
