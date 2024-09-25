# pydantic 应用

from fastapi import APIRouter
from typing import Union, Optional
from datetime import date
from pydantic import BaseModel, Field, validator
from typing import List
app03 = APIRouter()


class User(BaseModel):
    # name: str = Field(pattern="^a")
    name: str
    age: int = Field(default=0, gt=0, lt=100)
    birthday: Union[date, None] = Field(default_factory=date.today)
    friends: List[str] = []
    description: Optional[str] = None

    @validator("name")
    def name_must_be_alpha(cls, value):
        assert value.isalpha(), "name must be alphanumeric"
        return value


@app03.post('/data')
async def date(user: User):
    print(user.name)
    print(user.age)
    print(user.birthday)
    print(user.friends)
    return {

    }
