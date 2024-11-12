import os

import uvicorn
from fastapi import FastAPI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes


# os.environ['http_proxy'] = '127.0.0.1:8080'
# os.environ['https_proxy'] = '127.0.0.1:8080'
#
#
# os.environ['LANGCHAIN_TRACING_V2'] = "true"
# os.environ['LANGCHAIN_API_KEY'] = "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"


# LangChain调用百炼
def get_response():
    # 创建模型
    llm = ChatOpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如果您没有配置环境变量，请在此处用您的API Key进行替换
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope base_url
        model="qwen-plus"
    )
    # 准备提示 prompt
    messages = [
            SystemMessage(content="请将以下内容翻译成英文"),
            HumanMessage(content="你是人类吗")
    ]
    # result = llm.invoke(messages)
    # 简单的解析相应数据
    # parser = StrOutputParser()
    # print(result)
    # print(parser.invoke(result))

    # 创建返回数据的解析器
    parser = StrOutputParser()

    # 定义提示模版

    prompt_toolkit = ChatPromptTemplate.from_messages([
        ("system", "请将下面内容翻译成{language}"),
        ("user", "{text}")
    ])

    # 得到链
    chain = prompt_toolkit | llm | parser
    # 直接使用chain来调用
    print(chain.invoke({'language': "日文", 'text': "耳鼻喉科大夫"}))

    # 把我们的程序部署成服务
    # 创建fastapi的应用
    app = FastAPI(title="myLangChainDemo", version="1.0.0", description="LanChainDemo")

    add_routes(
        app,
        chain,
        path="/chainDemo"
    )

    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    get_response()
