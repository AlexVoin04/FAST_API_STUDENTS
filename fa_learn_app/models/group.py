import datetime
import uuid
from typing import Optional
from pydantic import BaseModel


class BaseGroup(BaseModel):
    """Базовый класс для описагия продукта"""

    name :str

class GroupOut(BaseGroup):
    """Класс описывает продукт, который отправляется пользователю (без секретной информации)"""

    id :uuid.UUID
