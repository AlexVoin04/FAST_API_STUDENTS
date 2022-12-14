from fastapi import FastAPI
from fa_learn_app.routers import student

def set_routers(app :FastAPI):
    app.include_router(student.router,prefix = "", tags=['students'])