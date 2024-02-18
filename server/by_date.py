from dotenv import load_dotenv
import http.client
import datetime
import os

# Load environmental variables
load_dotenv()

headers = {
    "x-rapidapi-host": "v3.football.api-sports.io",
    "x-rapidapi-key": os.getenv("X_RAPIDAPI_KEY"),
}
conn = http.client.HTTPSConnection("v3.football.api-sports.io")

# Get today's date in the correct format
timezone = "Asia/Bangkok"
today = datetime.date.today().strftime("%Y-%m-%d")
league = 39  # English Premier League

# Append your queries here
conn.request(
    "GET",
    f"/fixtures?timezone={timezone}&league={league}&date={today}",
    headers=headers,
)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))  # Write data to the terminal

# Write to a file
with open("fixtures.json", "w") as f:
    f.write(data.decode("utf-8"))

print("Data written to fixtures.json")
