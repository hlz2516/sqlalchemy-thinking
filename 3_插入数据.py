from sqlalchemy import *
from create_table import *
from datetime import datetime

eng = create_engine("mysql+pymysql://root:sbkj1234@localhost:3306/Test",echo=True)
#一次插入一条数据
curTime = datetime.now()
# stmt = insert(Account).values(LoginName="张三",Password="123",DataStatus="1",Age=18,CreateTime=curTime)
stmt = Account.insert().values(LoginName="张三",Password="123",DataStatus="1",Age=18,CreateTime=curTime)

#一次插入多条数据
stmt2 = Account.insert().values([
    {"LoginName":"李四","Password":"456","DataStatus":"1","Age":30,"CreateTime":curTime},
    {"LoginName":"王五","Password":"789","DataStatus":"1","Age":25,"CreateTime":curTime}
    ])

stmt3 = Role.insert().values(
    [
        {"RoleName":"Admin"},
        {"RoleName":"User"},
        {"RoleName":"Test"},
    ]
)

stmt4 = P_Function.insert().values(
    [
        {"FunctionName":"查询"},
        {"FunctionName":"修改"},
        {"FunctionName":"删除"},
        {"FunctionName":"添加"}
    ]
)

stmt5 = Role_Function.insert().values(
    [
        {"RoleID":1,"FunctionID":1},
        {"RoleID":1,"FunctionID":2},
        {"RoleID":1,"FunctionID":3},
        {"RoleID":1,"FunctionID":4},
        {"RoleID":2,"FunctionID":1},
        {"RoleID":2,"FunctionID":4},
        {"RoleID":3,"FunctionID":1},
        {"RoleID":3,"FunctionID":2},
        {"RoleID":3,"FunctionID":4},
    ]
)

stmt6 = Role_Account.insert().values(
    [
        {"RoleID":1,"AccountID":1},
        {"RoleID":2,"AccountID":3},
        {"RoleID":2,"AccountID":4},
        {"RoleID":3,"AccountID":7},
        {"RoleID":3,"AccountID":8},
    ]
)

with eng.connect() as conn:
    result = conn.execute(stmt5)
    result = conn.execute(stmt6)
    conn.commit()
    # print(result.inserted_primary_key)

#另一种插入多条的方式
# with eng.connect() as conn:
#     result = conn.execute(insert(Account),
#     [
#         {"LoginName":"老六","Password":"321","DataStatus":"1","Age":19,"CreateTime":curTime},
#         {"LoginName":"裴七","Password":"654","DataStatus":"1","Age":23,"CreateTime":curTime}
#     ])
#     conn.commit()
#     print(result.inserted_primary_key_rows)