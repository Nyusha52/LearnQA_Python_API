import allure
import requests

from lib.assertions import Assertions
from lib.base_case import BaseCase

@allure.epic('Get cases')
class TestUserGet(BaseCase):
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_user_details_as_someone_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        if user_id_from_auth_method > 1:
            response2 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method - 1}",
                                     headers={"x-csrf-token": self.token},
                                     cookies={"auth_sid": self.auth_sid}
                                     )
        else:
            response2 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method + 1}",
                                     headers={"x-csrf-token": self.token},
                                     cookies={"auth_sid": self.auth_sid}
                                     )

        expected_fields = ['password', 'firstName', 'lastName', 'email']
        Assertions.assert_json_has_key(response2, 'username')
        Assertions.assert_json_has_not_keys(response2, expected_fields)

