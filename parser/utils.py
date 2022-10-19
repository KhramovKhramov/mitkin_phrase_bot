import httpx

def get_html(url):
    headers =  {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0'
    }
    try:
        result = httpx.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except (httpx.RequestError, ValueError):
        print('Сетевая ошибка')
        return False

def write_content(text):
    with open('titles.txt', 'a', encoding='utf-8') as f:
        #f.write(f'{title}\n')
        #f.write(anons)
        f.write(text)