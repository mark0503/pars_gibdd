import requests
from bs4 import BeautifulSoup as bs
import mysql.connector


conn = mysql.connector.connect(host='localhost',
                         database='rusprofile',
                         user='sammy',
                         password='Password1.')
cursor = conn.cursor()


URL = f'https://xn--90adear.xn--p1ai/news/271/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15'}

def get_data(url):
    data = requests.get(url, headers=HEADERS)
    return data

def pars():
    number_page = 1
    while True:
        URL = f'https://xn--90adear.xn--p1ai/news/{number_page}/'
        html = get_data(URL).text
        soup = bs(html, 'html.parser')
        if soup.find_all('div', class_='sl-item-title'):
            items = soup.find_all('div', class_='sl-item-title')
            for i in items:
                item = i.find('div', class_='sl-item-text').get_text()
                title = i.find('a', class_='news-popup e-popup').get_text()
                for div in i.find_all('a', href=True):
                    name = div['href']
                    res_ref = 'https://xn--90adear.xn--p1ai'+name
                print (f'Ссылка на статью: {res_ref}')
                print(title.strip())
                print(item.strip())
                print('----------------')
            number_page += 1
        else:
            break

pars()