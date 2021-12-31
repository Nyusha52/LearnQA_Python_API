import allure

from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


@allure.epic('Edit cases')
class TestUserEdit(BaseCase):

    @allure.description('This is setup part')
    def setup(self):
        register_data = self.prepare_registration_data()
        response = MyRequests.post("/user", data=register_data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        self.email = register_data["email"]
        self.first_name = register_data["firstName"]
        self.password = register_data["password"]
        self.user_id = self.get_json_value(response, "id")
        self.login_data = {
            'email': self.email,
            'password': self.password
        }

        response1 = MyRequests.post("/user/login", data=self.login_data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")

    @allure.description('This test trying to edit user')
    def test_edit_created_user(self):
        new_name = "Changed Name"

        response = MyRequests.put(f"/user/{self.user_id}",
                                  headers={"x-csrf-token": self.token},
                                  cookies={"auth_sid": self.auth_sid},
                                  data={"firstName": new_name})
        Assertions.assert_code_status(response, 200)

        response1 = MyRequests.get(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(
            response1,
            "firstName",
            new_name,
            "Wrong name of the user after edit")

    @allure.description('This test trying to edit unauthorized user')
    def test_edit_unauthorized_user(self):
        new_name = "New_name"

        response = MyRequests.put(f"/user/{self.user_id}",
                                  data={"firstName": new_name})
        Assertions.assert_code_status(response, 400)
        Assertions.assert_content(response, "Auth token not supplied")

    @allure.description('This test trying to edit user by another user')
    def test_edit_user_by_another_user(self):
        another_user_data = self.prepare_registration_data()
        response = MyRequests.post("/user", data=another_user_data)
        another_user_id = self.get_json_value(response, "id")
        another_username = another_user_data["username"]

        new_name = "Second User name"

        response1 = MyRequests.put(f"/user/{another_user_id}",
                                   headers={"x-csrf-token": self.token},
                                   cookies={"auth_sid": self.auth_sid},
                                   data={"username": new_name}
                                   )
        Assertions.assert_code_status(response1, 200)

        response2 = MyRequests.get(
            f"/user/{another_user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response2,
            "username",
            another_username,
            "Oops!Username was edit by first user!"
        )

    @allure.description('This test trying to put incorrect data in email')
    def test_edit_user_with_incorrect_email(self):
        incorrect_email = "exampleexample.com"
        response = MyRequests.put(f"/user/{self.user_id}",
                                  headers={"x-csrf-token": self.token},
                                  cookies={"auth_sid": self.auth_sid},
                                  data={"email": incorrect_email}
                                  )
        Assertions.assert_code_status(response, 400)
        Assertions.assert_content(response, "Invalid email format")

    @allure.description('This test trying to put only one symbol in firstName')
    def test_edit_user_with_one_symbol_in_firstname(self):
        new_name = 'a'
        response = MyRequests.put(f"/user/{self.user_id}",
                                  headers={"x-csrf-token": self.token},
                                  cookies={"auth_sid": self.auth_sid},
                                  data={"firstName": new_name}
                                  )

        Assertions.assert_code_status(response, 400)
        Assertions.assert_json_value_by_name(
            response,
            "error",
            "Too short value for field firstName",
            "Oops!Username was edit!"
        )