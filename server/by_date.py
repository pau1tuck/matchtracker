from dotenv import load_dotenv
import http.client
import datetime
import os

# import json

# Load environmental variables
load_dotenv()

headers = {
    "x-rapidapi-host": os.getenv("X_API_PROVIDER"),
    "x-rapidapi-key": os.getenv("X_RAPIDAPI_KEY"),
}
connection = http.client.HTTPSConnection("v3.football.api-sports.io")

# Get today's date and other variables in the correct format
timezone = "Europe/London"
today = datetime.date.today().strftime("%Y-%m-%d")  # e.g. 2024-02-18
league = 39  # English Premier League
season = 2023  # 2023/24

# Query parameters
connection.request(
    "GET",
    f"/fixtures?timezone={timezone}&league={league}&date={today}&season={season}",
    headers=headers,
)

res = connection.getresponse()
data = res.read()

print(data.decode("utf-8"))  # Write data to the terminal

# Write to a file
with open("fixtures.json", "w") as f:
    f.write(data.decode("utf-8"))

print("Data written to fixtures.json.")
