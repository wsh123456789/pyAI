from fastapi import FastAPI
import uvicorn
from app01.urls import app01
from app02.urls import app02
app = FastAPI()

app.include_router(app01, prefix="/app01", tags=["app01"])
app.include_router(app02, prefix="/app02", tags=["app02"])

if __name__ == '__main__':
    uvicorn.run("main_router:app", host='127.0.0.1', port=8080, reload=True)