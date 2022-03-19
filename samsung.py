import json
from bs4 import BeautifulSoup
import requests

#model_name = "SM-A525FLVDSER"
model_name = "QE85QN85AAUXRU"

site_link = "https://www.samsung.com/ru/support/model/" + model_name + "/"
headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.4.837 Yowser/2.5 Safari/537.36"}

site_text = BeautifulSoup(requests.get(site_link, headers=headers).text, "html.parser")
content_objs = json.loads(site_text.find("li", attrs={'data-sdf-prop':'contents'}).text)

for content_obj in content_objs["manuals"]:
    print("download " + content_obj["fileName"])
    url = content_obj["downloadUrl"]
    r = requests.get(url, stream=True)
    with open("D:\YandexDisk\Privacy\Coding\scraping\\" + content_obj["fileName"], "wb") as fd:
        fd.write(r.content)
    fd.close()
