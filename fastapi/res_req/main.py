from fastapi import FastAPI
import uvicorn
from starlette.staticfiles import StaticFiles

from apps.base import app01
from apps.param_demo import app02
from apps.pydantic_demo import app03
from apps.form_demo import app04
from apps.file_demo import app05
from apps.request_demo import app06
from apps.response_demo import app07
app = FastAPI()

app.mount("/static", StaticFiles(directory="statics"), name="statics")

app.include_router(app01, prefix="/app01", tags=["app01 路径参数"])
app.include_router(app02, prefix="/app02", tags=["app02 查询参数"])
app.include_router(app03, prefix="/app03", tags=["app03 请求体"])
app.include_router(app04, prefix="/app04", tags=["app04 form表单"])
app.include_router(app05, prefix="/app05", tags=["app05 文件上传"])
app.include_router(app06, prefix="/app06", tags=["app06 request请求对象"])
app.include_router(app07, prefix="/app07", tags=["app06 request请求对象"])

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8080, reload=True)