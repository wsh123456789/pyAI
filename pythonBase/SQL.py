from pymysql import Connection
# 获取到MySQL数据库连接对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    # autocommit=True  # 设置自动提交
)
# 打印数据库软件信息
print(conn.get_server_info())
#获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('mydemo')
# 使用游标对象，执行sql语句
cursor.execute('select * from user')
# 获取查询结果
result: tuple = cursor.fetchall()
for row in result:
    print(row)
# 当对数据库数据进行改变时，需要提交操作
cursor.execute("insert into user (id, name, age, sex) values (4, '测试', 12, '男')")
conn.commit()
cursor.execute('select * from user')
result: tuple = cursor.fetchall()
for row in result:
    print(row)
# 关闭数据库连接
conn.close()