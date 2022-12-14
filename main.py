import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from fastapi import FastAPI
import uvicorn
from core.router import set_routers
from core import settings


app = FastAPI(title = "Learn FastAPI")


@app.on_event("startup")
async def startup():
    set_routers(app)
    
@app.on_event("shutdown")
async def shutdown():
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", port = settings.PORT, host = settings.HOST, reload = True)