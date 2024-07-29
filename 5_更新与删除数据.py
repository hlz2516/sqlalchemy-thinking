from sqlalchemy import *
from create_table import *
from datetime import datetime

eng = create_engine("mysql+pymysql://root:sbkj1234@localhost:3306/Test",echo=True)

stmt = update(Account).where(Account.c.LoginName == '裴七').values(LoginName = '佩奇')

# with eng.connect() as conn:
#     result = conn.execute(stmt)
#     conn.commit()

stmt2 = update(Account).where(Account.c.LoginName == '拜登').ordered_values((Account.c.LoginName,'托尼'),(Account.c.Age,40)) 

# with eng.connect() as conn:
#     result = conn.execute(stmt2)
#     conn.commit()

stmt3 = delete(Account).where(Account.c.LoginName == '托尼')

with eng.connect() as conn:
    result = conn.execute(stmt3)
    conn.commit()
    print(result.rowcount) # 可以获取到更新或者删除结果记录的行数