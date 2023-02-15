import requests
import re


numbers_list = []
with open('dataset_24476_3.txt', 'r') as numbers:
    for line in numbers:
        numbers_list.append(line.strip())
numbers.close()
url_api = "http://numbersapi.com/" + ",".join(numbers_list) + "/math"
params = {
    "json": "true"
}
response = requests.get(url=url_api, params=params)
# response = requests.get(url_api)
print(response.url)
data = response.json()
print(
    *map(
        lambda x:
            "Interesting"
            if re.search(r"(unremarkable|Boring|missing a fact|uninteresting)", data[x], re.IGNORECASE) is None
            else "Boring",
        numbers_list
    ),
    sep='\n')
