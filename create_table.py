# 该内容为第二节，因为其他内容可能引用该模块，因此文件名需按照模块规范取名
from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
# 一些知识点：
# sqlalchemy分为两类API：Core和ORM，其中ORM建立在Core之上
# ORM相对Core提供了一个额外的配置层，允许将用户定义的Python类映射到表和其他构造，以及具有持久性的session
# 因此建表也有两种建法，core style和orm style。这里我们以core风格为主，orm了解即可。

# core style
eng = create_engine("mysql+pymysql://root:sbkj1234@localhost:3306/Test",echo=True)
metaData = MetaData() #这是一个字典集合，key为Table对象中设置的表名，value为该Table对象(a Python dictionary that stores a series of Table objects keyed to their string name.)

Role = Table(
    "Role",
    metaData,
    Column("RoleID",Integer,primary_key=True,autoincrement=True),
    Column("RoleName",String(255),nullable=False),
)

Account = Table(
    "Account",
    metaData,
    Column("ID",Integer,primary_key=True,autoincrement=True),
    Column("LoginName",String(50),nullable=False),
    Column("Password",String(64),nullable=True),
    Column("DataStatus",String(1),nullable=True),
    Column("Age",Integer),
    Column("CreateTime",DateTime)
)

P_Function = Table(
    "P_Function",
    metaData,
    Column("FunctionID",Integer,primary_key=True,autoincrement=True),
    Column("FunctionName",String(200),nullable=False),
)

Role_Account = Table(
    "Role_Account",
    metaData,
    Column("RoleID",Integer,primary_key=True,autoincrement=True),
    Column("AccountID",Integer,primary_key=True)
)

Role_Function = Table(
    "Role_Function",
    metaData,
    Column("RoleID",Integer,primary_key=True,autoincrement=True),
    Column("FunctionID",Integer,primary_key=True)
)

metaData.create_all(eng)# 执行该代码会创建上述表结构（如果表不存在的情况下）

# ORM style
# class Base(DeclarativeBase):
#     pass

# class Role(Base):
#     __tablename__ = "Role"
#     RoleID:Mapped[int] = mapped_column(primary_key=True)
#     RoleName:Mapped[str] = mapped_column(String(255))

#     def __repr__(self) -> str:
#         return f"RoleID:{self.RoleID} RoleNmae:{self.RoleName}"

# Base.metadata.create_all(eng)