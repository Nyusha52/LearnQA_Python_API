import allure
from requests import Response
import json

from lib.base_case import BaseCase


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}' "
        assert name in response_as_dict, f"response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}' "
        assert name in response_as_dict, f"response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}' "

        for name in names:
            assert name in response_as_dict, f"response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}' "
        assert name not in response_as_dict, f"response JSON shouldn't have key '{name}. But it's present'"

    @staticmethod
    def assert_json_has_not_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}' "

        for name in names:
             assert name not in response_as_dict, f"response JSON shouldn't have key '{names}. But it's present'"

    @staticmethod
    def assert_response_content(response: Response, expected_content):
        assert response.content.decode("utf-8") == expected_content, f"Unexpected response content {response.content}."

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        with allure.step(f"Assert response has status code '{expected_status_code}'"):
            assert response.status_code == expected_status_code, \
                (f"Unexpected status code! Expected:{expected_status_code}. "
                 f"Actual:{response.status_code}")

    @staticmethod
    def assert_has_text_in(response: Response, expected_text: str):
        with allure.step(f"Assert response has text '{expected_text}'"):
            assert expected_text in response.text, \
                (f"Unexpected text! Expected: {expected_text}. "
                 f"Actual: {response.text}")


    @staticmethod
    def assert_login_user(response: Response):
        with allure.step("Assert login user"):
            user_id = BaseCase.get_json_value(response, "user_id")
            assert user_id != 0, f"User whith id '{user_id}' is not authorize."


    @staticmethod
    def assert_create_user(response: Response):
        with allure.step("Assert user successful create"):
            Assertions.assert_code_status(response, 200)
            Assertions.assert_json_has_key(response, 'id')


    @staticmethod
    def assert_user_not_found(response: Response):
        with allure.step("Assert response user not found"):
            Assertions.assert_code_status(response, 404)
            Assertions.assert_has_text_in(response, 'User not found')