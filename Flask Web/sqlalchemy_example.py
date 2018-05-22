from sqlalchemy import create_engine

host = '127.0.0.1'
port = '3306'
database = 'db'
username = 'root'
password = '123456'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/db?charset=utf8'
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo = True)

# with engine.connect() as con:
#     con.execute('drop table if exists users')
#     con.execute('create table users(id int primary key auto_increment, name varchar(24))')
#     con.execute('insert into users(name) values(\'jack\')')
#     con.execute('insert into users(name) values(\'joe\')')
#     rs = con.execute('select * from users')
#     for row in rs:
#         print(row)




