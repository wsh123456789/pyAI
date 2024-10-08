# 模板语法
import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi import Form, File, UploadFile
from typing import List, Union
from fastapi import Request
from pydantic import BaseModel, EmailStr, validator
from fastapi.templating import Jinja2Templates

# app08 = APIRouter()

templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/modelDemo")
def model_demo(request: Request):
    name = "root"
    books = ["金瓶梅", "聊斋", "剪灯新话", "国色天香"]
    return templates.TemplateResponse(
        "model_demo.html",  # 模板文件
        {
            "request": request,
            "username": name,
            "password": "123",
            "age": 30,
            "books": books,
            "booksDict": {
                "金瓶梅": {"price": 100, "publish": "苹果出版社"},
                "聊斋": {"price": 200, "publish": "橘子出版社"},
            }
        }  # context上下文对象，一个字典
    )


if __name__ == '__main__':
    uvicorn.run("model_demo:app", port=8090, reload=True)
