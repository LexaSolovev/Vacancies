import json

from src.Employer import Employer
from src.Salary import Salary


class Vacancy:

    id : int
    name : str
    url : str
    employer : Employer
    salary : Salary
    __full_data : dict

    __slots__ = ("id", "name", "url", "employer", "salary", "__full_data")

    def __init__(self, id, name, url, employer, salary, full_data = {}):
        self.id = id
        self.name = name
        self.url = url
        self.employer = employer
        self.salary = salary
        self.__full_data = full_data

    def __str__(self):

        return json.dumps(
            {
                "id" : self.id,
                "name" : self.name,
                "url" : self.url,
                "employer" : str(self.employer),
                "salary" : str(self.salary)
        },
            ensure_ascii=False,
            indent=4
        )

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.salary < other.salary
        raise TypeError(f"Попытка некорректного сравнения объекта "
                        f"{self.__class__.__name__} c объектом {other.__clas__.__name__}")
