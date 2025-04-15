from src.utils import filter_vacancies, get_area_id, get_vacancies_by_salary, search_id_by_name, sort_vacancies


def test_get_area_id():
    moscow_area_id = get_area_id("Москва")
    assert moscow_area_id == "1"


def test_search_id_by_name(areas):
    vilovatovo_id = search_id_by_name(areas, "Виловатово")
    russia_id = search_id_by_name(areas, "Россия")
    mari_el_id = search_id_by_name(areas, "Республика Марий Эл")
    assert vilovatovo_id == "4228"
    assert russia_id == "113"
    assert mari_el_id == "1620"


def test_sort_vacancies(vacancy1, vacancy2):
    vacancies = [vacancy1, vacancy2]
    assert sort_vacancies(vacancies) == [vacancy2, vacancy1]


def test_filter_vacancies(vacancy1, vacancy2):
    vacancies = [vacancy1, vacancy2]
    keywords = ["нужную"]
    filtered_vacancies = filter_vacancies(vacancies, keywords)
    assert filtered_vacancies == [vacancy1]


def test_get_vacancies_by_salary(vacancy1, vacancy2):
    vacancies = [vacancy2, vacancy1]
    assert get_vacancies_by_salary(vacancies, 90000, 99000) == []
    assert get_vacancies_by_salary(vacancies, 90000, 150000) == [vacancy1]
    assert get_vacancies_by_salary(vacancies, 90000, 200000) == [vacancy2, vacancy1]
    assert get_vacancies_by_salary(vacancies, 150000, 200000) == [vacancy2, vacancy1]
    assert get_vacancies_by_salary(vacancies, 150000, 250000) == [vacancy2, vacancy1]
    assert get_vacancies_by_salary(vacancies, 250000, 300000) == [vacancy2]
    assert get_vacancies_by_salary(vacancies, 300000, 350000) == [vacancy2]
    assert get_vacancies_by_salary(vacancies, 310000, 350000) == []
