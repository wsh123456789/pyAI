from langserve import RemoteRunnable

# 调用LangchainDemo的服务端
if __name__ == '__main__':
    client = RemoteRunnable("http://127.0.0.1:8000/chainDemo/")
    result = client.invoke({'language': "俄语", "text": "你好"})
    print(result)
