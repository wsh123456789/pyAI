import os

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

from LangChain.LangChain.models.QianFanModel import QianFanModel

os.environ['http_proxy'] = '127.0.0.1:7890'
os.environ['https_proxy'] = '127.0.0.1:7890'


os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = "123"

# 调用大语言模型
model = QianFanModel(api_key="123", base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

msg = [
    SystemMessage(content="请将以下内容翻译成英文"),
    HumanMessage(content="你是人类吗")
]

result = model.invoke(msg)
print(result)