from sqlalchemy import *
from create_table import *
from datetime import datetime

eng = create_engine("mysql+pymysql://root:sbkj1234@localhost:3306/Test",echo=True)
# 查询另一个表的字段插入到该表的指定字段
# 例如，我们想要让所有用户作为测试，那么就需要在Account表中先筛选出所有用户，然后指定ID字段插入到角色用户表中
select_stmt = select(Account.c.ID,text("3"))
insert_stmt = insert(Role_Account).from_select(
    ["AccountID","RoleID"],select_stmt
)
with eng.connect() as conn:
    result = conn.execute(insert_stmt)
    conn.commit()

# 如果一次性插入多条数据并想获取插入的记录的ID，可以使用returning语法(前提是你的数据库必须支持该语法，如PostgreSQL和SQL Server支持此特性。)
# curTime = datetime.now()
# stmt2 = Account.insert().values([
#     {"LoginName":"川普","Password":"456","DataStatus":"1","Age":60,"CreateTime":curTime},
#     {"LoginName":"拜登","Password":"789","DataStatus":"1","Age":70,"CreateTime":curTime}
#     ]).returning(Account.c.ID)
# with eng.connect() as conn:
#     result = conn.execute(stmt2)
#     conn.commit()
#     print(result)