from urllib.request import urlopen
import bs4
import datetime
import telegram

# Today date
dt = datetime.datetime.today()
YMD = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day)
weekday = dt.weekday()

# parsing function
def html_parsing():
    
    url = "http://www.jvision.ac.kr/vision/main/?menu=308&date="
    url + YMD
    print(url + YMD)
    html = urlopen(url + YMD)
    bs_obj = bs4.BeautifulSoup(html.read(),"html.parser")
    
    return bs_obj

# crawling function
def crawling():
    foodlists = bs_obj.findAll("div",{"class":"foodbox"})
    foodlist = []
    for i in foodlists:
        foodlist.append(i.text)
    print(foodlist[weekday*3+1])
    
    return foodlist[weekday*3+1]

# This function send lunch menu by your telegram.
def message_send():
    my_token = ""                           # insert your token
    bot = telegram.Bot(token = my_token)
    chat_id = ""                            # insert your chat_id
    
    bot.sendMessage(chat_id = chat_id, text=lunch)

# main code
if __name__ == "__main__":
    
    bs_obj =  html_parsing()
    lunch = crawling()
    message_send()