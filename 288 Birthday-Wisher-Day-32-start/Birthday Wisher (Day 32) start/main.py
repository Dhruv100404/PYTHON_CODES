import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("21ceuos020@ddu.ac.in", "Dhruv@104")

# message to be sent
message = "Subject:Helloo \n\n This is a message from python"

# sending the mail
s.sendmail("21ceuos020@ddu.ac.in", "dhruvthakkar104@gmail.com", message)

# terminating the session
s.quit()
