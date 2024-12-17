from pydantic import (
    BaseModel,
    field_validator,
)

from typing import Dict
from enum import Enum

import utils


class FieldType(Enum):
    email = "email"
    phone = "phone"
    date = "date"
    text = "text"


class FormTemplate(BaseModel):
    name: str
    fields: Dict[str, str]


class FormData(BaseModel):
    data: Dict[str, str] = None

    @field_validator("data", mode="before")
    def define_field_type(cls, values):
        for key, value in values.items():
            if utils.is_date(value):
                values[key] = FieldType.date.value
            elif utils.is_phone_number(value):
                values[key] = FieldType.phone.value
            elif utils.is_email(value):
                values[key] = FieldType.email.value
            else:
                values[key] = FieldType.text.value
        return values
