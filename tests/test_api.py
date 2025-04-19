from unittest.mock import patch

import pytest
import requests

from src.api import HeadHunterAPI


@pytest.fixture
def api():
    return HeadHunterAPI()


@patch('requests.get')
def test_get_vacancies_success(mock_get, api):
    # Подготовка данных для успешного запроса
    mock_response = {
        'items': [
            {'id': 1, 'name': 'Vacancy 1'},
            {'id': 2, 'name': 'Vacancy 2'}
        ]
    }
    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.status_code = 200

    # Выполнение метода get_vacancies
    vacancies = api.get_vacancies(keyword='test', page=0, to_page=1, per_page=2)

    # Проверка результатов
    assert len(vacancies) == 2
    assert vacancies[0]['name'] == 'Vacancy 1'
    assert vacancies[1]['name'] == 'Vacancy 2'


@patch('requests.get')
def test_get_vacancies_error(mock_get, api):
    # Подготовка данных для ошибочного запроса
    mock_get.return_value.status_code = 500

    # Проверка исключения при ошибке запроса
    with pytest.raises(requests.RequestException):
        api.get_vacancies(keyword='test', page=0, to_page=1, per_page=2)
