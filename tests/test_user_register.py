import allure
import pytest
import requests

from lib.base_case import BaseCase


@allure.epic('Register cases')
class TestUserRegister(BaseCase):
    @allure.description('This test trying create_user')
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

    @pytest.mark.parametrize(
        'password, username, firstName, lastName, email, statys', [
            [None,'learnqa', 'learnqa', 'learnqa', BaseCase().prepare_registration_data(), "The following required params are missed: password"],
            ['1234',None, 'learnqa', 'learnqa', BaseCase().prepare_registration_data(), "The following required params are missed: username"],
            ['1234','learnqa', None, 'learnqa', BaseCase().prepare_registration_data(), "The following required params are missed: firstName"],
            ['1234','learnqa', 'learnqa', None, BaseCase().prepare_registration_data(), "The following required params are missed: lastName"],
            ['1234','learnqa', 'learnqa', 'learnqa', None, "The following required params are missed: email"],
        ],
    )
    def test_create_user_without_field(self, password, username, firstName, lastName, email, statys):
        data = {
            'password': password,
            'username': username,
            'firstName': firstName,
            'lastName': lastName,
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Ошибка {response.status_code}"
        assert response.content.decode(
            "utf-8") == f"{statys}", f"Ошибка {response.content}"

    @allure.description('This test trying create_user')
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
