import json
import re

from config import PATH_AREAS
from src.api import HeadHunterAPI
from src.savers import JSONSaver
from src.vacancy import Vacancy


def search_id_by_name(areas: list[dict], name: str) -> str:
    """Рекурсивная функция для поиска area_id в дереве регионов"""
    for area in areas:
        if area["name"] == name:
            return area["id"]
        result = search_id_by_name(area.get("areas",[]), name)
        if result:
            return result


def get_area_id(name: str) -> str:
    """Функция для получения area_id по имени региона/города"""
    with open(PATH_AREAS) as f:
        areas = json.load(f)
    area_id = search_id_by_name(areas, name)
    return area_id


def sort_vacancies(vacancies_list: list[Vacancy]) -> list[Vacancy]:
    """Функция для сортировки вакансий по зарплате"""
    return sorted(vacancies_list, reverse=True)


def filter_vacancies(vacancies_list: list[Vacancy], filter_words : list[str]) -> list[Vacancy]:
    """ Функция для отбора вакансий из списка, в которых содержится хотя бы одно слово из списка filter_words"""
    filtered_vacancies = []
    for vacancy in vacancies_list:
        if vacancy.is_contain_words(filter_words):
            filtered_vacancies.append(vacancy)
    return filtered_vacancies

def get_vacancies_by_salary(vacancies_list: list[Vacancy], salary_begin : int, salary_end : int) -> list[Vacancy]:
    """
    Функция для получения списка вакансий, по которым зарплата находится в заданном диапазоне
    """
    result = []
    for vacancy in vacancies_list:
        if vacancy.salary.in_interval(salary_begin,salary_end):
            result.append(vacancy)
    return result

def print_vacancies(vacancies_list: list[Vacancy]) -> None:
    """ Функция для печати списка вакансий"""
    for vacancy in vacancies_list:
        print(vacancy)


def user_interaction():
    """Функция для работы с пользователем"""
    search_query = input("Введите поисковый запрос: ")
    filter_by_area = input("Введите регион для поиска (например: Москва, Россия, Нижегородская область):")
    area_id = get_area_id(filter_by_area)
    if area_id:
        print(f"Регион найден. Поиск осуществляется в регионе {filter_by_area}")
    else:
        print(f"Регион {filter_by_area} не найден. Поиск осуществляется без фильтрации по региону.")

    hh_api = HeadHunterAPI()
    print("Получение данных с сайта hh.ru...")
    hh_data = hh_api.get_vacancies(search_query, area=area_id)
    vacancies_list = sort_vacancies(Vacancy.cast_to_obj_list(hh_data))
    count_vacancies = len(vacancies_list)
    print(f"Данные успешно получены. По вашему запросу загружено {count_vacancies} вакансий")

    json_saver = JSONSaver()
    json_saver.save_vacancies(vacancies_list)

    while True:
        print("Выберите дальнейшие действия c полученными данными:")
        print("1. Вывести топ - N вакансий")
        print("2. Отфильтровать вакансии по ключевым словам")
        print("3. Отфильтровать вакансии по диапазону зарплат")
        print("4. Показать весь список загруженных вакансий")
        print("5. Завершить работу")
        user_input = input("Ваш выбор: ")
        if user_input == "1":
            top_n = int(input(f"Введите количество вакансий для вывода в топ N (от 1 до {count_vacancies}):"))
            if top_n > count_vacancies or top_n < 1:
                print ("Некорректное число!")
                continue
            for i in range(top_n):
                print(vacancies_list[i])

        elif user_input == "2":
            filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
            print_vacancies(filter_vacancies(vacancies_list, filter_words))

        elif user_input == "3":
            salary_input = input("Введите диапазон зарплат (например, 100000 - 150000): ")
            salary_interval = re.findall(r"\d+", salary_input)
            if (not salary_interval) or (len(salary_interval) != 2):
                print("Некорректный ввод диапазона зарплат!")
                continue
            int_salary = list(map(int,salary_interval))
            salary_begin = int_salary[0]
            salary_end = int_salary[1]
            if salary_begin >= salary_end:
                print("Некорректный ввод диапазона зарплат. Начальная зарплата должна быть меньше конечной.")
                continue
            print_vacancies(get_vacancies_by_salary(vacancies_list, salary_begin, salary_end))

        elif user_input == "4":
            print_vacancies(vacancies_list)

        elif user_input == "5":
            break

if __name__ == "__main__":
    user_interaction()