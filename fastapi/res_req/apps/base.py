from fastapi import APIRouter

app01 = APIRouter()


@app01.get('/food/{id}')
def food(id: int):
    print("id", id)
    return {'food': 'app01_food'}