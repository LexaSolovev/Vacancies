from abc import ABC, abstractmethod

class VacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def save_to_json(self, path):
        pass
