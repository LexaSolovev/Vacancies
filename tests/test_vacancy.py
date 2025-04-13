from src.vacancy import Vacancy


def test_cast_to_obj_list(vacancy1, vacancy2):
    vacancies_data = [
        {
            "id":1,
            "name":"Тестовая вакансия 1",
            "alternate_url":"https:какой_то_тестовый_урл_1",
            "employer": {"name":"Работодатель_1"},
            "salary":{
                "from":100000,
                "to":200000,
                "currency": "RUR"
            },
            "snippet":{
                "requirement":"Делать какую-то нужную работу 1"
            }
        },
        {
            "id": 2,
            "name": "Тестовая работа 2",
            "alternate_url": "https:какой_то_тестовый_урл_2",
            "employer": {"name": "Работодатель_2"},
            "salary": {
                "from": 200000,
                "to": 300000,
                "currency": "RUR"
            },
            "snippet": {
                "requirement": "Делать какую-то тестовую работу 2"
            }
        }
    ]
    vacancies_list = Vacancy.cast_to_obj_list(vacancies_data)
    vacancies_list_str = list(map(str, vacancies_list))
    assert vacancies_list_str == [str(vacancy1), str(vacancy2)]
