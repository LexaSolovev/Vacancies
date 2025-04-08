from abc import ABC, abstractmethod

class BaseVacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self, params):
        pass
