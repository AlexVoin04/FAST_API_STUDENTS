from fa_learn_app.repositories.student import StudentTmpRepository

TMP_PEROSITORY = StudentTmpRepository()

def get_student_repo() -> StudentTmpRepository:
    """Получение Product репозитория"""

    return TMP_PEROSITORY