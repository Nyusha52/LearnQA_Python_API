import requests

from lib.assertions import Assertions
from lib.base_case import BaseCase


class TestUserGet(BaseCase):
    def test_get_user_details_as_someone_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        self.auth_sid = self.get_cooke(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method-1}",
                                 headers={"x-csrf-token": self.token},
                                 cookies={"auth_sid": self.auth_sid}
                                 )

        Assertions.assert_json_has_key(response2, 'username')
        Assertions.assert_json_has_no_key(response2, 'email')
        Assertions.assert_json_has_no_key(response2, 'firstName')
        Assertions.assert_json_has_no_key(response2, 'lastName')
