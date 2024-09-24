import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

url = "https://stats.nba.com/stats/franchisehistory?LeagueID=00&Season=2023-24"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    "Referer": "https://stats.nba.com/",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token": "true"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser").prettify()
data = json.loads(soup)
franchise_history = data['resultSets'][0]
df_franchise_history = pd.DataFrame(franchise_history['rowSet'], columns=franchise_history['headers'])

caminho_csv = "./df_franchise_history.csv"

df_franchise_history.to_csv(caminho_csv, index=False)

print(df_franchise_history)


