# 选课系统
from typing import List

from pydantic import validator, BaseModel
from tortoise.models import Model
from tortoise import fields


class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, description="姓名")
    pwd = fields.CharField(max_length=100, description="密码")
    sno = fields.IntField(description="学号")

    # 一对多关系
    classroom = fields.ForeignKeyField("models.Classroom", related_name="students")
    
    # 多对多关系
    courses = fields.ManyToManyField("models.Course", related_name="students")


class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, description="教师姓名")
    pwd = fields.CharField(max_length=100)
    tno = fields.IntField()


class Classroom(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, description="班级名称")


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, description="课程名称")
    teacher = fields.ForeignKeyField("models.Teacher")
    addr = fields.CharField(max_length=100, description="教室")


class StudentIn(BaseModel):
    name: str
    pwd: str
    sno: int
    classroom_id: int
    courses: List[int] = []

    @validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), "name must be alpha"
        return value

    @validator("sno")
    def sno_must_alpha(cls, value):
        assert value > 0, "学号必须大于0"
        return value

