from fake_headers import Headers
import httpx

def get_html(url):
    headers = Headers(headers=True).generate()
    try:
        result = httpx.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except (httpx.RequestError, ValueError):
        print('Сетевая ошибка')
        return False

def write_content(text):
    with open('titles.txt', 'a', encoding='utf-8') as f:
        f.write(text)
