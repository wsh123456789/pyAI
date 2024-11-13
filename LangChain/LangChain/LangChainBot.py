import os

import uvicorn
from fastapi import FastAPI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langserve import add_routes
from torch.distributed.elastic.utils import store

# os.environ['http_proxy'] = '127.0.0.1:8080'
# os.environ['https_proxy'] = '127.0.0.1:8080'
#
#
# os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = "LangChainDemo"
# os.environ['LANGCHAIN_API_KEY'] = "key"


# LangChain调用百炼
# 聊天机器人创建
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
    ("system", "请{language}进你所能回答问题"),
])

# 得到链
chain = prompt_toolkit | llm | parser
# 直接使用chain来调用

# 保存历史记录
store = {}  # 所有用户的聊天信息都记录保存到store. key: sessionId, value: 历史聊天记录对象


def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


do_message = RunnableWithMessageHistory(
    chain,
    get_session_history,
    imput_message_key="my_msg")

config = {"configurable": {"session_id": "demo01"}}  # 定义当前会话的session_id

# 第一轮对话
resp = do_message.invoke(
    {
        "my_msg": [HumanMessage(content='你好啊！我是坤坤')],
        "language": "英文",
    },
    config=config
)

print(resp.content)


# 第二轮对话
resp = do_message.invoke(
    {
        "my_msg": [HumanMessage(content='请问我是谁')],
        "language": "中文",
    },
    config=config
)

print(resp.content)


