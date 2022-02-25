import requests

link = str("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")

response = requests.get(link)
response = requests.json()

