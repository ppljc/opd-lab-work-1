from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests


def parse():
    url = 'https://pypi.org/project/bs4/'  # передаем необходимы URL адрес
    proxies = {
        'http': 'http://proxy.omgtu:8080',
        'https': 'http://proxy.omgtu:8080'
    }
    page = requests.get(url, proxies=proxies)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code)  # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser")  # передаем страницу в bs4

    block = soup.findAll('div', class_='project-description')  # находим  контейнер с нужным классом
    description = ''
    for data in block:  # проходим циклом по содержимому контейнера
        if data.find('p'):  # находим тег <p>
            description = data.text  # записываем в переменную содержание тега

    print(description)
