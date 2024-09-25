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
        'url': request.url,
        'host': request.client.host,
        'user-agent': request.headers.get('User-Agent'),
        'cookie': request.cookies
    }
