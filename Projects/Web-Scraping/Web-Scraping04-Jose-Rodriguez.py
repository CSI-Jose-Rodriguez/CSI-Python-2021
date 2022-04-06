import requests
import bs4

webpage = requests.get("https://forecast.weather.gov/MapClick.php?lat=18.466330000000028&lon=-66.10472999999996#.YkroGyjMK5c")
soup = bs4.BeautifulSoup(webpage.content, "html.parser" )
sevenDay = soup.find(id="seven-day-forecast")
forecast_items = sevenDay.find_all(class_= "tombstone-container")
tonight = forecast_items[1]
print(tonight.prettify())
period = tonight.find(class_= "period-name").get_text()
Isolated = tonight.find(class_= "short-desc").get_text()
Tempature = tonight.find(class_= "temp temp-low").get_text()
print(period)
print(Isolated)
print(Tempature)