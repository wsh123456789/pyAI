from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Union
from fastapi import Request
from models import *

student_api = APIRouter()


@student_api.get('/index.html')
async def getIndex(request: Request):
    templates = Jinja2Templates(directory='templates')
    students = await Student.all()
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request,
            'students': students
        }
    )


@student_api.get('/')
async def getStudent():
    # 查询所有数据 all方法
    # students = await Student.all()
    # 过滤查询
    # students = await Student.get(id=0)  返回[ Student(),...]
    # students = await Student.filter(id=0) 返回 Student()
    # 模糊查询
    # students = await Student.filter(id__in=[0,1])
    # students = await Student.filter(id__gt2001)
    # students = await Student.filter(id__range=[1,1000])
    # values查询
    # students = await Student.all().values("name","sno")
    # students = await Student.all()
    # for student in students:
    #     print(student.name, student.sno)
    # 一对多查询
    stu = await Student.get(name="root")
    print(await stu.classroom.values("name"))
    print(await Student.all().values("name", "classroom__name"))
    # 多对多查询
    print(await stu.courses.all().values("name", "teacher__name"))
    print(await Student.all().values("name", "classroom__name", "courses__name", "courses__teacher__name"))
    # 多对多查询
    return {
        "操作": "查看所有学生"
    }


@student_api.post('/')
async def addStudent(student_in: StudentIn):

    # 添加到数据库
    # 方式1
    # student = Student(name=student_in.name, pwd=student_in.pwd, sno=student_in.sno, classroom_id=student_in.classroom_id)
    # await student.save()  # 插入数据库
    # 方式2
    student = await Student.create(name=student_in.name, pwd=student_in.pwd, sno=student_in.sno, classroom_id=student_in.classroom_id)

    # 多对多关系
    choose_courses = await Course.filter(id__in=student_in.courses)
    await student.courses.add(*choose_courses)
    return student


@student_api.get('/{student_id}')
async def getStudentById(student_id: int):
    student = await Student.get(student_id)
    return student


@student_api.put('/{student_id}')
async def updateStudentById(student_id: int, student_in: StudentIn):
    # 将传入的 Pydantic 模型转换为字典
    data = student_in.dict()

    # 从字典中取出课程信息并删除 'courses' 键
    courses = data.pop("courses")

    # 使用过滤器根据学生 ID 更新学生信息
    await Student.filter(id=student_in).update(**data)

    # 设置多对多课程关系
    edit = Student.get(id=student_id)

    # 查找当前学生选择的课程
    choose_courses = Course.filter(id__in=edit.courses)

    # 清除当前学生的所有课程
    await edit.courses.clear()

    # 添加新的课程到学生的课程列表
    await edit.courses.add(*choose_courses)

    # 返回操作结果
    return {
        "操作": f"更新id为{student_id}学生"
    }


@student_api.delete('/{student_id}')
async def deleteStudentById(student_id: int):
    delete_count = await Student.get(id=student_id).delete()
    if not delete_count:
        raise HTTPException(status_code=404, detail=f"主键为{student_id}的学生不存在")
    return {
        "操作": f"已删除id为{student_id}学生"
    }


