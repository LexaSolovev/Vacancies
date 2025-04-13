import json
import os.path

from config import PATH_DATA
from src.BaseSaver import BaseSaver
from src.Vacancy import Vacancy


class JSONSaver(BaseSaver):

    def __init__(self, file_name: str = "vacancies.json"):
        path = os.path.join(PATH_DATA, file_name)
        self.__path = path

    def get_data(self, keywords : str) -> list[Vacancy]:
        with open(self.__path) as f:
            vacancies_data = json.load(f)
        keywords_list = keywords.split()
        result = []
        for vacancy in vacancies_data:
            vacancy_str = json.dumps(vacancy, ensure_ascii=False)
            for word in keywords_list:
                if word in vacancy_str:
                    result.append(vacancy)
        return Vacancy.cast_to_obj_list(result)

    def add_vacancy(self, vacancy: Vacancy):
        with open(self.__path, "r") as f:
            vacancies_data = json.load(f)
        for vacancy_dict in vacancies_data:
            if vacancy_dict["id"] == vacancy.id:
                return
        vacancies_data.append(vacancy.to_dict())
        with open(self.__path, "w") as f:
            json.dump(vacancies_data, f, ensure_ascii=False, indent=4)

    def save_vacancies(self, vacancies : list[Vacancy]):
        with open(self.__path, "w") as f:
            json.dump([x.to_dict() for x in vacancies], f, indent=4, ensure_ascii=False)

    def delete_vacancy(self, vacancy: Vacancy|int):
        with open(self.__path, "r") as f:
            vacancies_data = json.load(f)
        for vacancy_dict in vacancies_data:
            if vacancy_dict["id"] == vacancy.id:
                vacancies_data.remove(vacancy_dict)
                with open(self.__path, "w") as f:
                    json.dump(vacancies_data, f, ensure_ascii=False, indent=4)
                return
