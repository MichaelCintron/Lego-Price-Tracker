import requests
from bs4 import BeautifulSoup


# Access webpage's HTML locally to avoid spamming Lego.com
with open("/home/michaelc/PycharmProjects/Lego_Prices/HTML_Docs/cat_owl_html_source.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# Or access the webpage's HTML and parse it directly
# url = 'https://www.lego.com/en-us/product/71475'
# # using headers to speed up response time
# # https://stackoverflow.com/questions/62599036/python-requests-is-slow-and-takes-very-long-to-complete-http-or-https-request
# headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
# response = requests.get(url, headers=headers)
# response_text = response.text
# soup = BeautifulSoup(response_text, 'html.parser')


# get the price of the Lego set from Lego.com
# <meta property="product:price:amount" content="49.99"/>
prices = soup.find_all("meta", property='product:price:amount')

# print(prices)
for price in prices:
    print(price)
    print(price.get("content"))


# in the interest of not spamming lego's website, can I
# just use the raw html file that I downloaded in its place?
# YES YOU CAN: Make sure you download the webpage's HTML, NOT THE HTML
# FOR THE 'view-source-page' PAGE!!

# so now I have a program that can fetch the price of a given lego set, how do I
# go about checking if it is on sale?

# might be time to start git-iffing my project and breaking the program into
# serperate functions and classes so I can have a 'working' version of the program
# and a testing environment. Also would like to start Agile-ing the project too

# John notes:
# build a pipeline
#     send from repo to online place (like AWS) automatically so that I don't have
#     to manually compile code
# push to an online place
# trunk based dev
# kanban board w/ user stories

