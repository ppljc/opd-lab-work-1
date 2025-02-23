from bs4 import BeautifulSoup
import requests


def parse():
    url = 'https://moscow.shop.megafon.ru/mobile/apple'
    proxies = {
        'http': 'http://proxy.omgtu:8080',
        'https': 'http://proxy.omgtu:8080'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }

    prices = []

    for i in range(1, 6):
        page = requests.get(f'{url}?page={i}', proxies=proxies, headers=headers)

        soup = BeautifulSoup(page.text, "html.parser")

        block = soup.findAll('span', class_='b-price-good-list__value b-price__value')
        for data in block:
            prices.append(int(data.text.replace(' ', '').replace('\n', '')))

    print(
        f'MIN = {min(prices)}\n'
        f'MAX = {max(prices)}\n'
        f'AVG = {sum(prices) / len(prices)}'
    )
