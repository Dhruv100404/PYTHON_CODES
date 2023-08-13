from twilio.rest import Client
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
twilio_number = "+13863380827"
twilio_sid = "AC726d8f58be464a9f250e92efcdc9ad33"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
api_key = "377D7BO5PKC5UJ9R"
twilio_token = "3380db24de1ccfc13aa6c20a48a30b92"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": api_key,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (60min)"]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
print(data_list)
yesterday_closing = yesterday_data["4. close"]
day_before_yesterday = data_list[16]
day_before_closing = day_before_yesterday["4. close"]

difference = abs(float(yesterday_closing) - float(day_before_closing))
print(difference)

avg = abs(float(yesterday_closing) + float(day_before_closing)/2)

percentage = abs((difference/avg)*100)

print(percentage)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


news_key = "a6f30fd11d814e56bb7194921cb62652"
# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage > 3:

    parameters = {
        "apikey": news_key,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=parameters)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    message = f"There is a big movement going on in the stock just have a look at the {up_down} and the company {COMPANY_NAME}"
    client = Client(twilio_sid, twilio_token)

    # TODO 8. - Send each article as a separate message via Twilio.

    message = client.messages.create(
        body= message,
        from_=twilio_number,
        to="+919662725700"
        )

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
