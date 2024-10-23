# request应用

from fastapi import APIRouter
from fastapi import Form, File, UploadFile
from typing import List
from fastapi import Request

import os

app06 = APIRouter()


# 请求体
@app06.post('/getRequest')
async def get_request(request: Request):
    return {
        'url': request.url,  # 请求URL
        'host': request.client.host,  # 请求IP
        'user-agent': request.headers.get('User-Agent'),  # 请求宿主
        'cookie': request.cookies
    }
