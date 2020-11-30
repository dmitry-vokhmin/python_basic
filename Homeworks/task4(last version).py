import time
import requests
from Homeworks import data_base
from Homeworks import models


class ParserAll:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
    }
    params = {
        'store': '',
        'records_per_page': 40,
        'page': 1,
        'categories': '',
    }

    def __init__(self, start_url):
        self.start_url = start_url
        self.data_base = data_base.DataBase("sqlite:///5ka.db") #// - обозначение url, /(третий) - относительный путь к данной директории

    def run(self):
        for products in self.parse(self.start_url):
            for product in products:
                self.data_base.create_product({
                    "id": product["id"],
                    "name": product["name"],
                    "img_link": product["img_link"],
                }, models.Product)

    def _get(self, *args, **kwargs):
        while True:
            response = requests.get(*args, **kwargs)
            if response.status_code != 200:
                time.sleep(0.3)
                continue
            return response

    def parse(self, url, params=None):
        if not params:
            params = self.params
        while url:
            response = self._get(url, headers=self.headers, params=params)
            if params:
                params = {}
            data: dict = response.json()
            url = data['next']
            yield data['results']


class ParserCatalog(ParserAll):

    def __init__(self, start_url, category_url):
        self.category_url = category_url
        super().__init__(start_url)

    def get_categories(self, url):
        response = self._get(url, headers=self.headers)
        return response.json()

    def run(self):
        for category in self.get_categories(self.category_url):
            self.data_base.create_category({
                "code": int(category["parent_group_code"]),
                "name": category["parent_group_name"],
            }, models.Category)

            self.params['categories'] = category['parent_group_code']

            for products in self.parse(self.start_url):
                for product in products:
                    self.data_base.create_product({
                        "id": product["id"],
                        "name": product["name"],
                        "img_link": product["img_link"],
                        "category_code": int(category["parent_group_code"]),
                        "old_price": product["current_prices"]["price_reg__min"],
                        "new_price": product["current_prices"]["price_promo__min"],
                        "promo_id": product["promo"]["id"],
                    }, models.Product)
                    self.data_base.create_promo({
                        "id": product["promo"]["id"],
                        "date_begin": product["promo"]["date_begin"],
                        "date_end": product["promo"]["date_end"]
                    }, models.Promo)


if __name__ == '__main__':
    parser = ParserCatalog('https://5ka.ru/api/v2/special_offers/', 'https://5ka.ru/api/v2/categories/')
    parser.run()
    print("End")
