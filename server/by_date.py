import http.client
import datetime

# Get today's date in the correct format
today = datetime.date.today().strftime("%Y-%m-%d")

timezone = "Asia/Bangkok"

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    "x-rapidapi-host": "v3.football.api-sports.io",
    "x-rapidapi-key": "XxXxXxXxXxXxXxXxXxXxXxXx",  # Make sure to replace this with your actual API key
}

# Append your queries here
conn.request(
    "GET", f"/fixtures?timezone={timezone}&league=39&date={today}", headers=headers
)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
