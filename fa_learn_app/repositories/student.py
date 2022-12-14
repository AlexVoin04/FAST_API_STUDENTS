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

    def create(self, student :StudentIn) -> StudentOut:
        raise NotImplementedError

    def update(self, id : uuid.UUID, student :StudentIn) -> StudentOut:
        raise NotImplementedError

    def delete(self, id :uuid.UUID) -> StudentOut:
        raise NotImplementedError

class StudentTmpRepository(BaseStudentRepository):
    """Реализация продукта с временным хранилищем в объектк Dict"""

    def __init__(self,):

        #Временное хранилище
        self._dict_students :Dict[uuid.UUID, StudentStorage] = {}

    def get_by_id(self, id :uuid.UUID) -> Optional[StudentOut]:
        """Получение проукта по id"""

        student :StudentStorage = self._dict_students.get(id, None)
        if student is None:
            return None
        student_out :StudentOut = convert_student_storage_to_out(student)
        return student_out

    def get_all(self, limit: int, skip: int) -> List[StudentOut]:
        """Получение всех продуктов"""

        student_out_list :List[StudentOut] = []
        for _, student in self._dict_students.items():
            student_out_list.append(convert_student_storage_to_out(student))
        return student_out_list[skip:skip+limit]

    def create(self, student: StudentIn) -> StudentOut:
        """Создание продукта"""

        student_storage :StudentStorage = convert_student_in_to_storage(student)
        self._dict_students.update({student_storage.id: student_storage})
        student_out :StudentOut = convert_student_storage_to_out(student_storage)
        return student_out


    def update(self, id :uuid.UUID, student_new :StudentIn) -> Optional[StudentOut]:
        """Обновление продукта"""

        student :StudentStorage = self._dict_students.get(id)
        if student is None:
            return None
        student_uptdate :StudentOut = update_student_in_to_storage(id, student_new)
        self._dict_students.update({student_uptdate.id: student_uptdate})
        student_out: StudentOut = convert_student_storage_to_out(student_uptdate)
        return student_out

    def delete(self, id :uuid.UUID) -> str:
        """Удаление объекта по id"""
        
        student :StudentStorage = self._dict_students.get(id)
        if student is None:
            return None
        self._dict_students.pop(id, None)
        return f"Продукт с id: {id} удален"