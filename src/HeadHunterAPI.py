import json
import os.path

import requests

from config import PATH_DATA
from src.VacancyAPI import VacancyAPI


class HeadHunterAPI(VacancyAPI):

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword, page=0, to_page=20, per_page=100, area=None):
        self.params['text'] = keyword
        self.params['page'] = page
        self.params['per_page'] = per_page
        self.params['area'] = area
        while self.params.get('page') != to_page:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    def save_to_json(self, path):
        with open(path, "w") as f:
            json.dump(self.vacancies, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    hh = HeadHunterAPI()
    hh.get_vacancies("Python", area=1)
    print(hh.vacancies)
    path_to_json = os.path.join(PATH_DATA, "vacansies.json")
    hh.save_to_json(path_to_json)