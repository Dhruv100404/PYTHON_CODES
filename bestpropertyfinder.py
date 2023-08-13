import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.zillow.com/tx/rentals/?searchQueryState=%7B%22usersSearchTerm%22%3A%22382421%22%2C%22mapBounds%22" \
      "%3A%7B%22north%22%3A36.45899619515125%2C%22east%22%3A-91.13947293663948%2C%22south%22%3A24.94887974745121%2C" \
      "%22west%22%3A-108.40998074913948%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B" \
      "%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C" \
      "%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22" \
      "%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max" \
      "%22%3A2000%7D%2C%22price%22%3A%7B%22max%22%3A404576%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C" \
      "%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54%2C" \
      "%22regionType%22%3A2%7D%5D%2C%22pagination%22%3A%7B%7D%7D "
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, "html.parser")
prices = []
price = soup.select(class_=".property-card-data")
prices.append(price)
print(prices)


