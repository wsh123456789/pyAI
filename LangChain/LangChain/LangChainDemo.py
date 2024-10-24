import os

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

#
# os.environ['http_proxy'] = '127.0.0.1:8080'
# os.environ['https_proxy'] = '127.0.0.1:8080'
#
#
# os.environ['LANGCHAIN_TRACING_V2'] = "true"
# os.environ['LANGCHAIN_API_KEY'] = "123"


# LangChain调用百炼
def get_response():
    llm = ChatOpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如果您没有配置环境变量，请在此处用您的API Key进行替换
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope base_url
        model="qwen-plus"
    )
    messages = [
            SystemMessage(content="请将以下内容翻译成英文"),
            HumanMessage(content="你是人类吗")
    ]
    response = llm.invoke(messages)
    print(response)


if __name__ == "__main__":
    get_response()
