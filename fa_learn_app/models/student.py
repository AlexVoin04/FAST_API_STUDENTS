import datetime
import uuid
from typing import Optional
from pydantic import BaseModel


class BaseStudent(BaseModel):
    """Базовый класс для описагия продукта"""

    first_name :str
    last_name :str
    age :int
    birth_date :datetime.datetime
    login :datetime.datetime
    group_id :str


class StudentIn(BaseStudent):
    """Класс описывает продукт, отправляемый от пользователя"""

    password :str


class StudentOut(BaseStudent):
    """Класс описывает продукт, который отправляется пользователю (без секретной информации)"""

    id :uuid.UUID

class StudentStorage(BaseStudent):
    """Класс описывает хранение продукта в хранилище"""

    id :uuid.UUID
    password :str