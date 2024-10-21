import time

import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# 跨域请求
# 方式一 手写
# @app.middleware("http")
# async def CORSMiddleware(request: Request, call_next):
#     response = await call_next(request)
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     return response

# 方式二 引用fastapi自带的
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许访问的客户端IP端口
    allow_credentials=True,  # 需不需要进行认证
    allow_methods=["*"],  # 请求方式 GET POST等
    allow_headers=["*"],  # 请求头
)


# 中间件所做操作，当前界面的所有接口均会执行中间件操作，
# 可以在请求到达实际处理器之前或之后执行自定义逻辑，
# 例如身份验证、日志记录、修改请求或响应等。
# 中间件2
@app.middleware("http")
async def middleware1(request: Request, call_next):
    print("Middleware1 request")
    response = await call_next(request)
    print("Middleware1 response")
    return response


# 中间件1
@app.middleware("http")
async def middleware2(request: Request, call_next):
    # 记录请求开始时间
    start_time = time.time()
    print("Middleware2 request")
    # 做拦截操作 例如IP限制
    # if request.client.host in ["127.0.0.1"]:
    #     return Response(content="visit forbidden")
    if request.url.path in ["/user"]:
        return Response(content="visit forbidden")
    response = await call_next(request)
    print("Middleware2 response")
    # 记录请求结束时间
    end_time = time.time()
    # 计算请求时间存入请求头
    response.headers["X-Process-Time"] = str(end_time-start_time)
    return response


@app.get("/user")
def get_user():
    print("get_user")
    return {"user": "user"}


@app.post("/item/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8010, reload=True, workers=1)