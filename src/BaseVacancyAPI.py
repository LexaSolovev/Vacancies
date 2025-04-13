from abc import ABC, abstractmethod

class BaseVacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self, keyword, page, to_page, per_page, area):
        pass
