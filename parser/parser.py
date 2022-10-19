from bs4 import BeautifulSoup
from string import punctuation

from utils import get_html, write_content

def get_page_urls():
    url = 'https://asnta.ru/authors/vladimir-mitkin/?PAGEN_2='
    page_urls = []
    page_numbers = list(range(1, 75))
    for page_number in page_numbers:
        page_url = f'{url}{page_number}'
        page_urls.append(page_url)
    
    return page_urls
        

def get_items_urls():
    page_urls = get_page_urls()

    urls = []
    for url in page_urls:
        html = get_html(url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            all_items = soup.find('div', class_='news-center__items').findAll('div', class_='news-center__item')
            for item in all_items:
                url = item.find('a', class_='news-center__link')["href"]
                urls.append(url)

    return urls

def get_item_text():
    items_urls = get_items_urls()
    
    for url in items_urls:
        item_url = f'https://asnta.ru{url}'
        item = get_html(item_url)
        if item:
            soup = BeautifulSoup(item, 'html.parser')
            #title = soup.find('h1', class_='bread__title').text
            #anons = soup.find('h2', class_='news-detail__anons').text
            text = soup.find('div', class_='news-detail__text').text
            write_content(text)

if __name__ == '__main__':
    get_item_text()
