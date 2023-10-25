import requests

params = {
    "api_token": "???????",
    "language": "fr"
}
url = "https://api.marketaux.com/v1/news/all"
result = requests.get(url, params=params).json()
# print(result["data"][0])

titles = []
for article in result["data"]:    
    titles.append([article["published_at"], article["title"]])  
print(titles)