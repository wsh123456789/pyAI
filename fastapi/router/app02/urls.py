from fastapi import APIRouter

app02 = APIRouter()

@app02.get('/login')
def login():
    return {'user': 'admin', 'password': '123456'}

@app02.post('/reg')
def register():
    return {'user': 'admin', 'password': '123'}