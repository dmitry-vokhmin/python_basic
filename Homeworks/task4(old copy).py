import os
from pathlib import Path
import time
import json
import requests
from Homeworks import data_base


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

    file_structure = {
        "name": "",
        "code": "",
        "products": [],
    }

    def __init__(self, start_url, cat_url):
        self.start_url = start_url
        self.cat_url = cat_url
        self.data_base = data_base.DataBase("sqlite:///5ka.db")

    def run(self):
        for categories in self.parse_categories(self.cat_url):
            self.params['categories'] = categories['parent_group_code']
            self.data_base.create_category({
            "code": int(categories["code"]),
            "name": categories["name"],
        })
            for products in self.parse(self.start_url):
                for product in products:
                    self.data_base.create_product({
                "id": product["id"],
                "name": product["name"],
                "img_link": product["img_link"],
            })

    def _get(self, *args, **kwargs):
        while True:
            response = requests.get(*args, **kwargs)
            if response.status_code != 200:
                time.sleep(0.3)
                continue
            return response

    def parse_categories(self, url):
        response = self._get(url, headers=self.headers)
        cat_data = response.json()
        return cat_data

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

    def save(self, file_name):
        self.data_base.create_category({
            "code": int(self.file_structure["code"]),
            "name": self.file_structure["name"],
        })
        for product in self.file_structure["products"]:
            self.data_base.create_product({
                "id": product["id"],
                "name": product["name"],
                "img_link": product["img_link"],
            })
        # if self.file_structure["products"]:
        #     file_path = Path(__file__).parent.joinpath(f"{file_name}.json")
        #     file_path.write_text(json.dumps(self.file_structure, ensure_ascii=False))
        #     self.file_structure["products"].clear()



if __name__ == '__main__':
    parser = ParserAll('https://5ka.ru/api/v2/special_offers/', 'https://5ka.ru/api/v2/categories/')
    parser.run()