# response 应用

from fastapi import APIRouter
from fastapi import Form, File, UploadFile
from typing import List, Union
from fastapi import Request
from pydantic import BaseModel, EmailStr, validator

import os

app07 = APIRouter()


class UserInfo(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Union[str, None] = None


class UserOUt(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


# 响应体
@app07.post('/register', response_model=UserOUt)
async def register(user: UserInfo):
    return user


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


# response_model_exclude_unset=True 排除未设置的值
# response_model_exclude_none=True 排除nones的值
# response_model_exclude_defaults=True 排除有默认值的值
# response_model_exclude_include={"name","price"} 只显示某些字段的值
# response_model_exclude={"name","price"} 排除某些字段的值

@app07.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
