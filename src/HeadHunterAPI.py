import os.path

import requests

from config import PATH_DATA
from src.BaseVacancyAPI import BaseVacancyAPI


class HeadHunterAPI(BaseVacancyAPI):

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies_json = []


    def get_vacancies(self, keyword, page=0, to_page=20, per_page=100, area=None):
        self.params['text'] = keyword
        self.params['page'] = page
        self.params['per_page'] = per_page
        self.params['area'] = area
        while self.params.get('page') != to_page:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                vacancies_json = response.json()['items']
                self.__vacancies_json.extend(vacancies_json)
                self.params['page'] += 1
            else:
                raise requests.RequestException(f"Ошибка запроса. Cтатус код = {response.status_code}")
        return self.__vacancies_json
