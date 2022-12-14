from typing import List
import uuid
import requests
import random


BASE_URL = "http://localhost:8000"

def form_data_student() -> dict:
    """Формирование данных продукта"""

    return {
        "first_name": f"Name {random.randint(0,100000)}",
        "last_name": f"Surname {random.randint(0,100000)}",
        "age": f"Age {random.randint(16,80)}",
        "birth_date": f"Birth date {random.randint(1980,2006)}-{random.randint(1,12)}-{random.randint(1,28)}",
        "login": f"Login {random.randint(0,100000)}",
        "password": str(uuid.uuid4())
    }

def get_all_students() -> List[dict]:
    """Получение всех продуктов в система"""

    students = requests.get(BASE_URL+"/students")
    return students.json()

def get_student_by_id(id :uuid.UUID) -> dict:
    """Получение продукта по id"""

    student = requests.get(BASE_URL+"/student?id={id}")
    return student.json()

