from abc import ABC, abstractmethod

import requests


class VacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self, query: str):
        pass


class HeadHunterAPI(VacancyAPI):

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'city': 'Москва'}
        self.vacancies = []

    def get_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

if __name__ == "__main__":
    hh = HeadHunterAPI()
    hh.get_vacancies("Python")
    print(hh.vacancies)