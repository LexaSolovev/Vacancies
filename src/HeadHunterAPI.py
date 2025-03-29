import json
import os.path

import requests

from config import PATH_DATA
from src.Employer import Employer
from src.Salary import Salary
from src.Vacancy import Vacancy
from src.VacancyAPI import VacancyAPI


class HeadHunterAPI(VacancyAPI):

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies_json = []
        self.vacancies = []

    def get_vacancies(self, keyword, page=0, to_page=20, per_page=100, area=None):
        self.params['text'] = keyword
        self.params['page'] = page
        self.params['per_page'] = per_page
        self.params['area'] = area
        while self.params.get('page') != to_page:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies_json = response.json()['items']
            self.__vacancies_json.extend(vacancies_json)
            self.params['page'] += 1
        self.__parse_vacancies()

    def save_to_json(self, path):
        with open(path, "w") as f:
            json.dump(self.__vacancies_json, f, indent=4, ensure_ascii=False)

    def __parse_vacancies(self):
        for vacancy in self.__vacancies_json:
            employer_json = vacancy.get('employer', {})
            employer = Employer(
                employer_json.get('id', -1),
                employer_json.get('name', 'Работодатель неизвестен'),
                employer_json.get('url', "")
            )

            salary_json = vacancy.get('salary', {}) if vacancy.get('salary', {}) else {}
            salary = Salary(
                salary_json.get('from', 0),
                salary_json.get('to', 0),
                salary_json.get('currency', "")
            )

            self.vacancies.append(
                Vacancy(
                    vacancy.get('id'),
                    vacancy.get('name'),
                    vacancy.get('url'),
                    employer,
                    salary
                )
            )


if __name__ == "__main__":
    hh = HeadHunterAPI()
    hh.get_vacancies("Python", area=1)
    for x in hh.vacancies:
        print(x)
    path_to_json = os.path.join(PATH_DATA, "vacansies.json")
    hh.save_to_json(path_to_json)