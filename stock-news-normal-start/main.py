import requests
import smtplib
stock = "Tesla"


my_email = "Your Email"
my_password = "Your Password"

api_key = "API KEY"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&slice=year1month1&outputsize=full&apikey={api_key}"


newsurl = ('https://newsapi.org/v2/everything?'
       'q=Tesla Inc&'
       'from=2022-11-04&'
       'sortBy=popularity&'
       'apiKey=3115c2dccdfa45c2929042af5b3095e4')

news_response = requests.get(newsurl)
p=(news_response.json()["articles"])

three_articles = p[:1]


response = requests.get(url=url)
dt = response.json()
ndt = dt["Time Series (Daily)"]
data_list = [value for (key, value) in ndt.items()]
yesterdat_closing_price = data_list[0]["4. close"]
day_before_yesterday = data_list[1]["4. close"]

difference = (float(yesterdat_closing_price)-float(day_before_yesterday))
diffpercent = (difference/float(yesterdat_closing_price)) *100


if diffpercent > 5:
    formatted_list = [f"Headline: {p['title']}, \nBrief: {p['description']}" for p in three_articles]
    message=formatted_list[0]
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(my_email, my_password)
  
    connection.sendmail(to_addrs=my_email, from_addr=my_email, msg=f"Subject:{stock}: {round(diffpercent,2)}%\n\n {message}")
    

   
