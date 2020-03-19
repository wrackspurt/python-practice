"""
Task 3
Написать скрапер для каталога товаров магазина http://www.podrastayka.ru/ Скрапер должен уметь находить список категорий
товаров (меню слева), предлагать юзеру выбор категории, а дальше пробегаться по всем подкатегориям выбранной категории и
выводить товары со скидой (те где цена перечеркнута). Например, скрапер находит товар со скидкой, и выводит в консоль
строку в виде "LION Стиральный порошок "ТОП - Сушка в помещении" 900 г: 400.00 руб.( 450 руб. )".
"""

import requests
from lxml import html


URL = 'http://www.podrastayka.ru/'
MENU = '//div[@id = "bar1"]//a[@class="linkpodmenu"]'
COSMETICS = URL + 'index.php?categoryID=291'


def get_submenu_urls(menu_path):
    submenu_urls = []
    for t in tree.xpath(menu_path):
        submenu_urls.append(t.attrib['href'])
    return submenu_urls


def get_bargains_from_submenu(path):
    request = requests.get(URL + path)
    body = html.fromstring(request.text)
    prices = body.xpath('//div[@style="font-size:11px;"]')
    results = []
    for p in prices:
        if p.xpath('.//div[@class="prod_price"]/strike/text()'):
            price = p.xpath('.//div[@class="prod_price"]/text()')
            elem = p.xpath('.//div[@class="prod_descr"]/text()')
            results.append(f'{str(elem[0]).strip()}: {str(price[0]).strip()}')
    return results


def get_urls(path):
    request = requests.get(path)
    body = html.fromstring(request.text)
    urls = []
    links = body.xpath('//a[@class="linkpodmenucategory"]')
    for l in links:
        urls.append(URL + l.attrib['href'])
    return urls


def get_bargains_from_subcategory(path):
    links = get_urls(path)
    results = []
    for l in links:
        request = requests.get(l)
        body = html.fromstring(request.text)
        prices = body.xpath('//div[@style="font-size:11px;"]')
        for p in prices:
            if p.xpath('.//div[@class="prod_price"]/strike/text()'):
                price = p.xpath('.//div[@class="prod_price"]/text()')
                elem = p.xpath('.//div[@class="prod_descr"]/text()')
                results.append(f'{str(elem[0]).strip()}: {str(price[0]).strip()}')
    return results


if __name__ == '__main__':
    response = requests.get(URL)

    tree = html.fromstring(response.text)

    submenu = tree.xpath(MENU + '/text()')

    print(f'привет! вот категории товаров интернет-магазина {URL[11:25]}: ')
    for i in range(0, len(submenu)):
        print(i + 1, '-', submenu[i])

    try:
        user = int(input('\nпожалуйста, выбери одну из них (просто введи номер категории): '))

        choice = {
            1: get_bargains_from_subcategory(URL + get_submenu_urls(MENU)[0]),
            2: get_bargains_from_subcategory(URL + get_submenu_urls(MENU)[1]),
            3: get_bargains_from_submenu(get_submenu_urls(MENU)[2]),
            4: get_bargains_from_submenu(get_submenu_urls(MENU)[3]),
            5: get_bargains_from_submenu(get_submenu_urls(MENU)[4]),
            6: get_bargains_from_submenu(get_submenu_urls(MENU)[5]),
            7: get_bargains_from_subcategory(COSMETICS)
        }

        print('\nв данной категории имеются следующие товары по скидке: ')

        if len(choice[user]) == 0:
            print('упс! кажется, в этой категории нет товаров по скидке.')
        else:
            for c in range(0, len(choice[user])):
                print(f'{c + 1}) {choice[user][c]}')
    except KeyError:
        print('такой категории в списке нет.')
    except ValueError:
        print('некорректный ввод.')
