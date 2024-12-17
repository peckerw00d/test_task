from email_validator import validate_email, EmailNotValidError
from datetime import datetime
import phonenumbers


def is_email(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False


def is_phone_number(phone_number: str) -> bool:
    try:
        phone_number = phonenumbers.parse(phone_number, "RU")
        return phonenumbers.is_valid_number(phone_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False


def is_date(date: str) -> bool:
    try:
        return bool(datetime.strptime(date, "%Y-%m-%d"))
    except ValueError:
        return False
