import requests

BASE_URL = "http://localhost:8000"


def test_get_form():
    data = {
        "data": {
            "first_field": "test_email@gmail.com",
            "second_field": "88005553535",
            "third_field": "2002-12-07",
        }
    }
    response = requests.post(f"{BASE_URL}/get_form", json=data)
    print("GET FORM Response:", response.json())


if __name__ == "__main__":
    test_get_form()
