import json
import os.path

from config import PATH_DATA
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class BaseSaver(ABC):

    @abstractmethod
    def get_data(self, keywords) -> list[Vacancy]:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy|int):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy|int):
        pass

    @abstractmethod
    def save_vacancies(self, vacancies_list: list[Vacancy]):
        pass


class JSONSaver(BaseSaver):
    """
    Класс JSONSaver для хранения информации о вакансиях в файле формата json

    Свойства:
    __path - приватный атрибут для хранения пути файла

    Методы:
    get_data
    add_vacancy
    save_vacancies
    delete_vacancy
    """

    def __init__(self, file_name: str = "vacancies.json"):
        path = os.path.join(PATH_DATA, file_name)
        self.__path = path

    def get_data(self, keywords : str) -> list[Vacancy]:
        """
        Метод для получения данных из файла по ключевым словам.
        Возвращает список объектов класса Vacancy
        """
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

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Метод для добавления вакансии в файл.
        Добавляются только уникальные вакансии.
        """
        with open(self.__path, "r") as f:
            vacancies_data = json.load(f)
        for vacancy_dict in vacancies_data:
            if vacancy_dict["id"] == vacancy.id:
                return
        vacancies_data.append(vacancy.to_dict())
        with open(self.__path, "w") as f:
            json.dump(vacancies_data, f, ensure_ascii=False, indent=4)

    def save_vacancies(self, vacancies : list[Vacancy]) -> None:
        """Метод для сохранения списка вакансий в файл"""
        with open(self.__path, "w") as f:
            json.dump([x.to_dict() for x in vacancies], f, indent=4, ensure_ascii=False)

    def delete_vacancy(self, vacancy: Vacancy|int) -> None:
        """Метод для удаления вакансии из файла"""
        with open(self.__path, "r") as f:
            vacancies_data = json.load(f)
        for vacancy_dict in vacancies_data:
            if vacancy_dict["id"] == vacancy.id:
                vacancies_data.remove(vacancy_dict)
                with open(self.__path, "w") as f:
                    json.dump(vacancies_data, f, ensure_ascii=False, indent=4)
                return
