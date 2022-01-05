import allure
import pytest
import requests

from lib.base_case import BaseCase


@allure.epic('Register cases')
class TestUserRegister(BaseCase):
    data_with_one_empty_param = [
        ({'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'},
         'password'),
        ({'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'},
         'username'),
        ({'password': '123', 'username': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'},
         'firstName'),
        ({'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'email': 'vinkotov@example.com'},
         'lastName'),
        ({'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'}, 'email')
        ]

    @allure.description('This test trying create_user')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Ошибка {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Ошибка {response.content}"

    @allure.description('This test trying create_user')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_with_incorrect_email(self):
        email = 'vinkotovexample.com'
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Ошибка {response.status_code}"
        assert response.content.decode(
            "utf-8") == f"Invalid email format", f"Ошибка {response.content}"

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("data", data_with_one_empty_param)
    def test_create_user_without_field(self, data):
        data, empty_param = data

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Ошибка {response.status_code}"
        assert response.content.decode(
            "utf-8") == f"The following required params are missed: {empty_param}", f"Ошибка {response.content}"

    @allure.description('This test trying create_user')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_name_one_symbol(self):
        email = self.prepare_registration_data()
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName': 'l',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Ошибка {response.status_code}"
        assert response.content.decode(
            "utf-8") == f"The value of 'firstName' field is too short", f"Ошибка {response.content}"

    @allure.description('This test trying create_user')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_name_more_255_symbol(self):
        email = self.prepare_registration_data()
        data = {
            'password': '1234',
            'username': 'learnq'*50,
            'firstName': 'l',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Ошибка {response.status_code}"
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too long", f"Ошибка {response.content}"
