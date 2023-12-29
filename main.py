import requests
from send_email import send_email

api_key ="d709ccc1624a4f36adace0e4a97c57bc"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-11-29&sortBy=publishedAt&apiKey=d709ccc1624a4f36adace0e4a97c57bc&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
      if article["title"] is not None:
            body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)