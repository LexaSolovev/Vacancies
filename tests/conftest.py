import pytest

from src.vacancy import Vacancy

@pytest.fixture
def vacancy1():
    return Vacancy(
        1,
        "Тестовая вакансия 1",
        "https:какой_то_тестовый_урл_1",
        "Работодатель_1",
        100000,
        200000,
        "RUR",
        "Делать какую-то нужную работу 1"
    )


@pytest.fixture
def vacancy2():
    return Vacancy(
        2,
        "Тестовая работа 2",
        "https:какой_то_тестовый_урл_2",
        "Работодатель_2",
        200000,
        300000,
        "RUR",
        "Делать какую-то тестовую работу 2"
    )


@pytest.fixture
def areas():
    return [
        {
            "id":"113",
            "parent_id":None,
            "name":"Россия",
            "areas":[
                {
                    "id":"1620",
                    "parent_id":"113",
                    "name":"Республика Марий Эл",
                    "areas":[
                        {
                            "id":"4228",
                            "parent_id":"1620",
                            "name":"Виловатово",
                            "areas":[]
                        }]
                }]
        }]