from sqlalchemy import create_engine,text
engine = create_engine("mysql+pymysql://root:sbkj1234@localhost:3306/Test",echo=True)
try:
    with engine.connect() as connection:
        result = connection.execute(text('SELECT 1')) #使用该语句测试连接是否正常
        print("数据库连接正常！") 
except Exception as e:
    print(str(e))