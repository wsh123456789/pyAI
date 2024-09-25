# 文检传输应用

from fastapi import APIRouter
from fastapi import Form, File, UploadFile
from typing import List

import os

app05 = APIRouter()


# 适合小文件上传 单文件
@app05.post('/uploadFileBytes')
async def get_file(file: bytes = File()):
    print(file)
    return {
        'file': "file",
    }


# 适合小文件上传 多文件
@app05.post('/uploadFilesBytes')
async def get_files(files: list[bytes] = File()):
    print(files)
    return {
        'file': "file",
    }


@app05.post('/uploadFile')
async def upload_file(file: UploadFile):
    print(file)
    path = os.path.join("files", file.filename)
    # 文件保存
    with open(path, "wb") as f:
        for line in file.file:
            f.write(line)
    return {
        'file': "file",
    }


@app05.post('/uploadFiles')
async def upload_file(files: List[UploadFile]):
    print(files)
    for file in files:
        path = os.path.join("files", file.filename)
        # 文件保存
        with open(path, "wb") as f:
            for line in file.file:
                f.write(line)
    return {
        'file': "file",
    }


