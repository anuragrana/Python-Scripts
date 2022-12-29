import requests
from bs4 import BeautifulSoup
import sys
import time


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36"
}

site_link_count = 0

for i in range(1, 201):
    url = "http://websitelists.in/website-list-" + str(i) + ".html"
    response = requests.get(url, headers = headers)
    if response.status_code != 200:
        print(url + str(response.status_code))
        continue
    
    soup = BeautifulSoup(response.text, 'lxml')
    sites = soup.find_all("td",{"class": "web_width"})
    
    links = ""
    for site in sites:
        site = site.find("a")["href"]
        links += site + "\n"
        site_link_count += 1

    with open("one_million_websites.txt", "a") as f:
        f.write(links)
    
    print(str(site_link_count) + " links found")

    time.sleep(1)
    
    
