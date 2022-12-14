from typing import List, Dict, Optional
import uuid
from fa_learn_app.models.student import StudentIn, StudentOut, StudentStorage
from fa_learn_app.utils.repository_utils import convert_student_storage_to_out, convert_student_in_to_storage, update_student_in_to_storage


class BaseStudentRepository:
    """Базовый класс для реализации функционала работы с продуктами"""

    def get_by_id(self, id :uuid.UUID | int) -> StudentOut:
        raise NotImplementedError

    def get_all(self, limit :int, skip :int) -> List[StudentOut]:
        raise NotImplementedError

    def create(self, product :StudentIn) -> StudentOut:
        raise NotImplementedError

    def update(self, id : uuid.UUID, product :StudentIn) -> StudentOut:
        raise NotImplementedError

    def delete(self, id :uuid.UUID) -> StudentOut:
        raise NotImplementedError

class StudentTmpRepository(BaseStudentRepository):
    """Реализация продукта с временным хранилищем в объектк Dict"""

    def __init__(self,):

        #Временное хранилище
        self._dict_products :Dict[uuid.UUID, StudentStorage] = {}

    def get_by_id(self, id :uuid.UUID) -> Optional[StudentOut]:
        """Получение проукта по id"""

        product :StudentStorage = self._dict_products.get(id, None)
        if product is None:
            return None
        product_out :StudentOut = convert_student_storage_to_out(product)
        return product_out

    def get_all(self, limit: int, skip: int) -> List[StudentOut]:
        """Получение всех продуктов"""

        product_out_list :List[StudentOut] = []
        for _, product in self._dict_products.items():
            product_out_list.append(convert_student_storage_to_out(product))
        return product_out_list[skip:skip+limit]

    def create(self, product: StudentIn) -> StudentOut:
        """Создание продукта"""

        product_storage :StudentStorage = convert_student_in_to_storage(product)
        self._dict_products.update({product_storage.id: product_storage})
        product_out :StudentOut = convert_student_storage_to_out(product_storage)
        return product_out


    def update(self, id :uuid.UUID, product_new :StudentIn) -> Optional[StudentOut]:
        """Обновление продукта"""

        product :StudentStorage = self._dict_products.get(id)
        if product is None:
            return None
        product_uptdate :StudentOut = update_student_in_to_storage(id, product_new)
        self._dict_products.update({product_uptdate.id: product_uptdate})
        product_out: StudentOut = convert_student_storage_to_out(product_uptdate)
        return product_out

    def delete(self, id :uuid.UUID) -> str:
        """Удаление объекта по id"""
        
        product :StudentStorage = self._dict_products.get(id)
        if product is None:
            return None
        self._dict_products.pop(id, None)
        return f"Продукт с id: {id} удален"