import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
import yagmail
import keyring

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
actual = price.split("$")[1]

factual = float(actual)
print(factual)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if factual < BUY_PRICE:
    message = f"{title} is now {price}"
    sender_email = "dt9662725700@gmail.com"

    import smtplib
    import ssl

    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()  # check connection
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # check connection
        server.login(sender_email, "Dhruv@100404")

        # Send email here
        server.sendmail(sender_email, "dhruvthakkar104@gmail.com", message.as_string())

    except Exception as e:
        # Print any error messages
        print(e)
    finally:
        server.quit()
