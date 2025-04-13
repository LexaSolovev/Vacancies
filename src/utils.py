import json

from config import PATH_AREAS
from src.HeadHunterAPI import HeadHunterAPI
from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy


def search_id_by_name(areas, name):
    for area in areas:
        if area["name"] == name:
            return area["id"]
        result = search_id_by_name(area.get("areas",[]), name)
        if result:
            return result

    return None


def get_area_id(name: str):
    with open(PATH_AREAS) as f:
        areas = json.load(f)
    area_id = search_id_by_name(areas, name)
    return area_id


def sort_vacancies(vacancies_list: list[Vacancy]):
    return sorted(vacancies_list, reverse=True)


def user_interaction():
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
    vacancies_list = Vacancy.cast_to_obj_list(hh_data)
    print(f"Данные успешно получены. По вашему запросу загружено {len(vacancies_list)} вакансий")

    json_saver = JSONSaver()
    json_saver.save_vacancies(vacancies_list)

    while True:
        print("Выберите дальнейшие действия:")
        print("1. Вывести топ - N вакансий")
        print("2. Отфильтровать вакансии по ключевым словам")
        print("3. Отфильтровать вакансии по диапазону зарплат")
        print("4. Показать весь список загруженных вакансий")
        print("5. Завершить работу")
        user_input = input("Ваш выбор: ")
        if user_input == "1":
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))


    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    print(get_area_id("Россия"))