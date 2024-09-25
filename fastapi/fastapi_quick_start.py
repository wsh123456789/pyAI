from fastapi import FastAPI
app = FastAPI()

# get请求做查看，delete做删除，put和patch做修改，post做添加
# async 异步请求的支持
@app.get("/home")
async def home():
    return {"Hello": "World"}

@app.get("/shop")
async def shop():
    return {"shopId": "apple"}

# 控制台使用 uvicorn 启动服务 uvicorn fastapi_quick_start:app --reload --port 8080
# 也可以依靠代码执行
# 可以访问 /docs 接口看到接口文档(自动生成swagger文档)
import uvicorn
if __name__ == '__main__':
    uvicorn.run("fastapi_quick_start:app", host='127.0.0.1', port=8080, reload=True)

# 路径操作装饰器方法参数
# tags=["接口文档标题"]
# summary="接口文档描述"
# description="item文档详情"
# response_description="响应注解"
# deprecated="false" 是否废弃使用，true是废弃，false不废弃
@app.post("/items",tags=["item测试接口"], summary="item文档描述", description="item文档详情", response_description="响应注解", deprecated="false")
async def test():
    return {"test": "demoItem"}
