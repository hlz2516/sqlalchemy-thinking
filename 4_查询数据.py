from sqlalchemy import *
from create_table import *
from datetime import datetime

eng = create_engine("mysql+pymysql://root:sbkj1234@localhost:3306/Test",echo=True)

stmt = select(Account).where(Account.c.LoginName == '李四')
with eng.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(row.ID)
        print(row.LoginName)
        print(row.Password)
    # 也可以用下面这种方式，因为有些情况下我们只需要取第一条记录
    # result = conn.execute(stmt).first()
    # print(result.ID)
    # print(result.LoginName)
    # print(result.Password)

# 查找年龄在20岁以上且id<5的名字
stmt2 = select(Account.c.LoginName).where(Account.c.ID < 5,Account.c.Age > 20) # 等价于下面这段查询
# stmt2 = select(Account.c.LoginName).where(and_(Account.c.ID < 5,Account.c.Age > 20))
with eng.connect() as conn:
    result = conn.execute(stmt2)
    for row in result:
        print(row)

# 查找年龄在20以下或者在65以上的且ID大于5的名字
stmt3 = select(Account.c.LoginName).where(
    and_(
        Account.c.ID > 5,
        or_(
            Account.c.Age < 20,
            Account.c.Age > 65
        )
    )
)
with eng.connect() as conn:
    result = conn.execute(stmt3)
    for row in result:
        print(row[0])

# 查找所有具有删除权限的角色（join）
# 先找到删除权限的ID
stmt_delID = select(P_Function.c.FunctionID).where(P_Function.c.FunctionName == '删除')
conn1 = eng.connect()
delID = conn1.execute(stmt_delID).first()[0]
# select的字段为Role的所有字段，Role表连接Role_Function表，并显式通过量表的RoleID字段进行连接
stmt4 = select(Role).select_from(Role).join(Role_Function,Role.c.RoleID == Role_Function.c.RoleID).where(Role_Function.c.FunctionID == delID)
res = conn1.execute(stmt4)
for row in res:
    print(row.RoleName)
conn1.close()

# 查找所有用户并按年龄升序排序
# stmt5 = select(Account).order_by(Account.c.Age.asc())

# 查询所有用户的数量
# select(func.count(Account.c.ID))

