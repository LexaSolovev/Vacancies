from src.salary import Salary

def test_salary_str():
    salary_from = Salary(100000)
    salary_to = Salary(0, 100000)
    salary_full = Salary(100000, 200000)
    salary_full_eur = Salary(1000, 2000, "EUR")
    salary_null = Salary()
    assert str(salary_from) == "от 100000 RUR"
    assert str(salary_to) == "до 100000 RUR"
    assert str(salary_full) == "100000 - 200000 RUR"
    assert str(salary_full_eur) == "1000 - 2000 EUR"
    assert str(salary_null) == "Зарплата не указана"


def test_salary_lt():
    salary_from = Salary(100000)
    salary_to = Salary(0, 100000)
    salary_full = Salary(100000, 200000)
    salary_high_to = Salary(100000, 300000)
    salary_high_from = Salary(150000, 200000)
    salary_null = Salary()
    assert salary_from < salary_full
    assert salary_to < salary_full
    assert salary_full < salary_high_to
    assert salary_full < salary_high_from
    assert salary_null < salary_from
    assert salary_null < salary_to
