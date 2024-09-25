from fastapi import APIRouter

app01 = APIRouter()

@app01.get('/food')
def food():
    return {'food': 'app01_food'}