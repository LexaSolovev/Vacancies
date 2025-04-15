from src.salary import Salary


class Vacancy:

    id : int
    name : str
    url : str
    employer : str
    salary : Salary
    description : str

    __slots__ = ("id", "name", "url", "employer", "salary", "description")

    def __init__(self, id, name, url, employer, salary_from, salary_to, currency, description):
        self.id = id
        self.name = name
        self.url = url
        self.employer = employer
        self.salary = Salary(salary_from, salary_to, currency)
        self.description = description

    @classmethod
    def cast_to_obj_list(cls, vacancies_data : list[dict]) -> list:
        vacancies_list = []
        for vacancy in vacancies_data:
            salary_info = vacancy["salary"]
            salary_from, salary_to, currency = cls.__validate_salary(salary_info)
            vacancies_list.append(
                cls(
                    vacancy["id"],
                    vacancy["name"],
                    vacancy["alternate_url"],
                    vacancy["employer"]["name"],
                    salary_from,
                    salary_to,
                    currency,
                    vacancy.get("snippet",{}).get("requirement")
                )
            )
        return vacancies_list

    @staticmethod
    def __validate_salary(salary_info: dict | None) -> tuple:
        """ Метод для валидации информации о зарплате, возвращает картеж (salary_from, salary_to, currency) """
        salary_from = 0
        salary_to = 0
        currency = "RUR"
        if salary_info:
            salary_from = salary_info["from"] if salary_info["from"] else 0
            salary_to = salary_info["to"] if salary_info["to"] else 0
            currency = salary_info["currency"] if salary_info["currency"] else "RUR"
        return salary_from, salary_to, currency

    def __str__(self):

        return (f"Вакансия: {self.name}\n"
                f"Ссылка: {self.url}\n"
                f"Организация: {self.employer}\n"
                f"Зарплата: {str(self.salary)}\n"
                f"Требования: {self.description}\n")


    def to_dict(self):
        return {
                "id" : self.id,
                "name" : self.name,
                "url" : self.url,
                "employer" : self.employer,
                "salary" : str(self.salary),
                "description" : self.description
        }

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.salary < other.salary
        raise TypeError(f"Попытка некорректного сравнения объекта "
                        f"{self.__class__.__name__} c объектом {other.__clas__.__name__}")

    def is_contain_words(self, keywords : list[str]) -> bool:
        self_str = str(self)
        for word in keywords:
            if word in self_str:
                return True
        return False