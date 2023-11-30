from bs4 import BeautifulSoup
import requests
import sqlite3 as sq

headers = {
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Referer': 'https://www.tsum.ru/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}


def create_tables():
    with sq.connect('products.db') as con:
        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand_and_name TEXT,
        price TEXT,
        description TEXT,
        product_link TEXT
        )''')


def get_url_clothes():
    for count in range(1, 2):
        url = f'https://www.tsum.ru/catalog/odezhda-2409/?sort=date&page={count}'

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find_all('div', class_='style__container___IPYI4')

        for i in data:
            url_clothes = r'https://www.tsum.ru/' + i.find('a').get('href')
            yield url_clothes


def get_product_info():
    for url_info in get_url_clothes():
        con = sq.connect('products.db')

        cur = con.cursor()

        new_response = requests.get(url_info, headers=headers)

        new_soup = BeautifulSoup(new_response.text, 'lxml')

        brand_and_name = new_soup.find('h1', class_='styles__productName___t3vA6').text
        price = new_soup.find('p', class_='style__price___l9Hm2').find('span').text.strip() + 'р.'
        info_product_data = new_soup.find('div', class_='style__infoBlocksRow___B0ZNv').find_all('li')
        product_link = url_info

        info_product_list = []
        for info_product_html in info_product_data:
            info_product = info_product_html.text
            info_product_list.append(info_product)

        description = '; '.join(info_product_list)

        cur.execute('''
                   INSERT INTO products (brand_and_name, price, description, product_link)
                   VALUES (?, ?, ?, ?)
               ''', (brand_and_name, price, description, product_link))

        con.commit()

        con.close()


def main():
    create_tables()

    get_product_info()


if __name__ == '__main__':
    main()




