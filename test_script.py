import requests

BASE_URL = "http://localhost:8000"


def test_get_form():
    data = {
        "data": {
            "email_field": "my_email@gmail.com",
            "phone_field": "88005553535",
            "date_field": "2021-10-28",
        }
    }
    response = requests.post(f"{BASE_URL}/get_form", json=data)
    print("GET FORM Response:", response.json())


if __name__ == "__main__":
    test_get_form()
