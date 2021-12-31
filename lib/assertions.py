from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"ошибка {response.text}"

        assert name in response_as_dict, f"ошибка {name}"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"ошибка {response.text}"

        assert name in response_as_dict, f"ошибка {name}"

    @staticmethod
    def assert_json_has_no_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"ошибка {response.text}"

        assert name not in response_as_dict, f"ошибка {name}"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"ошибка {response.text}"

        for name in names:
            assert name in response_as_dict, f"ошибка {name}"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, f"ошибка {response.status_code}"

    @staticmethod
    def assert_content(response: Response, expected_content):
        assert response.content.decode("utf-8") == expected_content, f"Unexpected response content {response.content}."
