import requests

api_key ="d709ccc1624a4f36adace0e4a97c57bc"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-11-29&" \
      "sortBy=publishedAt&apiKey=d709ccc1624a4f36adace0e4a97c57bc"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in  content["articles"]:
      print(article['title'])
      print(article['description'])