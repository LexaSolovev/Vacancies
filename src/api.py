import requests

from src.BaseVacancyAPI import BaseVacancyAPI


class HeadHunterAPI(BaseVacancyAPI):

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies_json = []


    def get_vacancies(self, keyword: str, page: int = 0, to_page: int = 20, per_page: int = 100, area: int = None):
        self.__params['text'] = keyword
        self.__params['page'] = page
        self.__params['per_page'] = per_page
        self.__params['area'] = area
        self.__vacancies_json = []
        while self.__params.get('page') != to_page:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                vacancies_json = response.json()['items']
                self.__vacancies_json.extend(vacancies_json)
                self.__params['page'] += 1
            else:
                raise requests.RequestException(f"Ошибка запроса. Cтатус код = {response.status_code}")
        return self.__vacancies_json
