# form表单应用

from fastapi import APIRouter
from fastapi import Form

app04 = APIRouter()


@app04.post('/regin')
async def regin(username: str = Form(), password: str = Form()):
    print(username, password)
    return {
        'username': username,
    }
