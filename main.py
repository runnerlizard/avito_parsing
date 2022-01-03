import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    buttons = soup.find_all('a', class_='pagination-page')[-1].get('href')
    pages = buttons.split('=')[-2].split('&')[0]
    return int(pages)


def get_info(html):
    soup = BeautifulSoup(html, 'lxml')
    info = soup.find('div', class_='items-items-kAJAg').find_all('div', id=True)
    print (info[0] + '\n')
    # with open('from_avito.csv', 'a') as f:
    #     writer = csv.writer(f)
    #     writer.writerow()
    #     print('parsed')


def main():
    url = 'https://www.avito.ru/cheboksary/avtomobili/audi-ASgBAgICAUTgtg3elyg?cd=1&p=1&radius=200'
    html = get_html(url)
    p = get_total_pages(html)
    urls = []
    for i in range(1, p):
        url = 'https://www.avito.ru/cheboksary/avtomobili/audi-ASgBAgICAUTgtg3elyg?cd=1&radius=200&p=' + str(i)
        html = get_html(url)
        get_info(html)


if __name__ == '__main__':
    main()