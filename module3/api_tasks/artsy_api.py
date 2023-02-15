import requests
import json


client_id = "488b24ed5cc1877e4547"
client_secret = "b567d9d22d2f3d36a43e0d5ad76032e3"
token_url = "https://api.artsy.net/api/tokens/xapp_token"
client_params = {
    "client_id": client_id,
    "client_secret": client_secret
}
artist_ids = []
with open("input", "r", encoding="utf8") as fin:
    for line in fin:
        artist_ids.append(line.strip())
fin.close()
result_list = []
# artist_ids = ["4d8b92b34eb68a1b2c0003f4", "537def3c139b21353f0006a6", "4e2ed576477cc70001006f99"]
token_response = requests.post(url=token_url, data=client_params)
token_data = json.loads(token_response.text)
token = token_data["token"]
headers = {"X-Xapp-Token": token}
for artist_id in artist_ids:
    artist_response = requests.get("https://api.artsy.net/api/artists/" + artist_id, headers=headers)
    artist_data = json.loads(artist_response.text)
    result_list.append((artist_data["sortable_name"], artist_data["birthday"]))
print(*list(map(lambda x: x[0], sorted(result_list, key=lambda x: (int(x[1]), x[0])))), sep='\n')
