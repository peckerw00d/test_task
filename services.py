from tinydb.table import Table

from models import FormData, FormTemplate
from db import templates_table


def get_templates():
    templates = [FormTemplate(**doc) for doc in templates_table.all()]
    return templates


def get_template(template_id: id):
    template = templates_table.get(doc_id=template_id)
    return template


def create_template(template: FormTemplate):
    templates_table.insert(template.model_dump())
    return template


def update_template(template_id: int, updated_template: FormTemplate):
    templates_table.update(updated_template.model_dump(), doc_ids=[template_id])
    return templates_table.get(doc_id=template_id)


def delete_template(template_id: int):
    templates_table.remove(doc_ids=[template_id])
    return f"Your template has been deleted"


def find_matching_templates(form_data: FormData, table: Table) -> str | dict[str, str]:
    processed_data = form_data.data

    for template in table.all():
        match = all(
            field_name in processed_data and processed_data[field_name] == field_type
            for field_name, field_type in template["fields"].items()
        )

        if match:
            return template["name"]

    return processed_data
