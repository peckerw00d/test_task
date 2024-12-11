from pydantic import (
    BaseModel,
    StringConstraints,
)

from typing import Dict, Annotated, List


class FieldModel(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1)]


class FormTemplate(BaseModel):
    name: str
    fields: List[FieldModel]


class FormData(BaseModel):
    data: Dict[str, str]
