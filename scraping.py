import requests
from bs4 import BeautifulSoup
import pickle

url = "https://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%81%AE%E5%A4%96%E5%9B%BD%E8%AA%9E%E5%90%8D%E4%B8%80%E8%A6%A7"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")


table_elements = soup.select("td")
whole_pokemon = int(len(soup.select("td")) / 8)

jap_en_pokemon_dict = {}
for i in range(whole_pokemon):
    n_pokemon = i * 8
    try:
        k, v = table_elements[n_pokemon+1].text, table_elements[n_pokemon+2].text.lower()
        if k[-1] == "\n":
            k = k[:-1]
        if v[-1] == "\n":
            v = v[:-1]
        jap_en_pokemon_dict[k] = v
    except:
        print(f"error!! {table_elements[n_pokemon].text, table_elements[n_pokemon+1].text}")


print(f"pokemon:{len(jap_en_pokemon_dict)}")

with open("jap_en_pokemon.pickle", mode="wb") as f:
    pickle.dump(jap_en_pokemon_dict, f)


