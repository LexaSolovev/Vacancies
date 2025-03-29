from src.Employer import Employer


class Vacancy:

    id : int
    name : str
    url : str
    employer : Employer
    salary : Salary

    def __init__(self, id, name, url, employer, salary):
        self.id = id
        self.name = name
        self.url = url
        self.employer = employer
        self.salary = salary