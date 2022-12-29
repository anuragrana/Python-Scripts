# Author - Anurag Rana

from bs4 import BeautifulSoup
import requests
import telegram
from config import telegram_token_news

def get_news_data(starting_url):
    news_data = []    
    response = requests.get(starting_url)
    soup = BeautifulSoup(response.text, 'lxml')
    element = soup.find(attrs={"class": "deQdld"})
    print(element)
    for c_wizi in element:
        data = {}
        a = c_wizi.find(attrs={"class":"nuEeue hzdq5d ME7ew"})
        if a:
            try:
                link = a.attrs["href"]
                text = a.string.strip()
            except Exception as e:
                print(e)
            if link and text:            
                data["link"] = link
                data["text"] = text
                news_data.append(data)

    return news_data
    

def get_msg(news_data):
    msg = "\n\n\n"
    for news_item in news_data:
        text = news_item["text"]
        link = news_item["link"]
        msg += text+'  [<a href="'+link+'">source</a>]'
        msg += "\n\n"
        
    return msg



bot = telegram.Bot(token=telegram_token_news)

urls = [
    'https://news.google.com/news/headlines/section/topic/NATION.hi_in/%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4?ned=hi_in&hl=hi',
    'https://news.google.com/news/headlines/section/topic/NATION.en_in/India?ned=in&hl=en-IN',
    'https://news.google.com/news/headlines/section/topic/ENTERTAINMENT.en_in/Entertainment?ned=in&hl=en-IN',
]

for url in urls:
    news_data = get_news_data(url)
    if len(news_data) > 0:
        msg = get_msg(news_data)
        status = bot.send_message(chat_id="@newsindiachannel", text=msg, parse_mode=telegram.ParseMode.HTML)        
        if status:            
            print(status)
    else:
        print("no new news")


