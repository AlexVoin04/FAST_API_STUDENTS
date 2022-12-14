import datetime
import uuid
from fa_learn_app.models.student import StudentStorage,StudentOut, StudentIn


def convert_student_storage_to_out(student : StudentStorage) -> StudentOut:
    """Производит конвертацию StudentStorage --> StudentOut"""

    tmp_dict:dict = student.dict()
    tmp_dict.pop("password", None)
    return StudentOut(**tmp_dict)

def convert_student_in_to_storage(student :StudentIn) -> StudentStorage:
    """Производит конвертацию StudentIn --> StudentStorage"""

    tmp_dict :dict = student.dict()
    student_storage = StudentStorage(id = uuid.uuid4(),
                                    **tmp_dict)
    return student_storage

def update_student_in_to_storage(old_id :uuid.UUID, student_update :StudentIn) -> StudentStorage:

    tmp_dict :dict = student_update.dict()
    student_storage = StudentStorage(id = old_id,
                                    **tmp_dict)
    return student_storage
                                    