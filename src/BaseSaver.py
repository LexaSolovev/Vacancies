from abc import ABC, abstractmethod

from src.Vacancy import Vacancy


class BaseSaver(ABC):

    @abstractmethod
    def get_data(self, params):
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