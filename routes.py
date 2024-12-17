from fastapi import APIRouter

from db import templates_table
from models import FormTemplate, FormData
import services

router = APIRouter(tags=["forms"])


@router.post("/get_form")
async def get_form(data: FormData):
    return services.find_matching_templates(form_data=data, table=templates_table)


@router.get("/get_templates")
async def get_templates():
    return services.get_templates()


@router.get("/get_template/{template_id}")
async def get_template(template_id: int):
    return services.get_template(template_id=template_id)


@router.post("/create_template")
async def create_template(template: FormTemplate):
    return services.create_template(template=template)


@router.put("/update_template/{template_id}")
async def update_template(template_id: int, updated_template: FormTemplate):
    return services.update_template(
        template_id=template_id, updated_template=updated_template
    )


@router.delete("/delete_template/{template_id}")
async def delete_template(template_id: int):
    return services.delete_template(template_id=template_id)
