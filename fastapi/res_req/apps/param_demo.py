from fastapi import APIRouter
from typing import Union, Optional
app02 = APIRouter()

# 设置查询参数，如果有默认参数，为非必填项
# Union[str, None] 可为none类型也可为str 等同于 Optional[str]
@app02.get('/login')
async def login(user: str, pwd=None, type_demo: Union[str, None] = None):
    return {'user': user, 'password': pwd, "type_demo": type_demo}

@app02.post('/reg')
def register():
    return {'user': 'admin', 'password': '123'}