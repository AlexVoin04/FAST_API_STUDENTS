from typing import List
import uuid
from fastapi import APIRouter, Depends
from fa_learn_app.dependencies import get_student_repo
from fa_learn_app.models.student import StudentIn, StudentOut
from fa_learn_app.repositories.student import BaseStudentRepository


router = APIRouter()

@router.get("/students", response_model = List[StudentOut])
async def get_students(
    product_repo :BaseStudentRepository = Depends(get_student_repo),
    limit :int = 100,
    skip :int = 0
    ):
    return product_repo.get_all(limit=limit, skip=skip)

@router.get("/student", response_model = StudentOut)
async def get_student(
    id :uuid.UUID,
    product_repo :BaseStudentRepository = Depends(get_student_repo),
    ):
    return product_repo.get_by_id(id)

@router.post("/student", response_model = StudentOut)
async def create_student(
    product_in :StudentIn,
    product_repo :BaseStudentRepository = Depends(get_student_repo),
    ):
    return product_repo.create(product_in)

@router.put("/student", response_model = StudentOut)
async def update_student(
    id :uuid.UUID,
    product_in: StudentIn,
    product_repo :BaseStudentRepository = Depends(get_student_repo),
    ):
    return product_repo.update(id, product_in)

@router.delete("/student", response_model = str)
async def delete_student(
    id :uuid.UUID,
    product_repo :BaseStudentRepository = Depends(get_student_repo),
    ):
    return product_repo.delete(id)