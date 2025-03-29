import json

from src.Employer import Employer
from src.Salary import Salary


class Vacancy:

    id : int
    name : str
    url : str
    employer : Employer
    salary : Salary

    def __init__(self, id, name, url, employer, salary, full_data):
        self.id = id
        self.name = name
        self.url = url
        self.employer = employer
        self.salary = salary
        self.full_data = full_data

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
