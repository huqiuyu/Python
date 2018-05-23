from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, Text,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


host = '127.0.0.1'
port = '3306'
database = 'db'
username = 'root'
password = '123456'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/db?charset=utf8'
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo = True)
Base = declarative_base(engine)
session = sessionmaker(engine)()
# with engine.connect() as con:
#     con.execute('drop table if exists users')
#     con.execute('create table users(id int primary key auto_increment, name varchar(24))')
#     con.execute('insert into users(name) values(\'jack\')')
#     con.execute('insert into users(name) values(\'joe\')')
#     rs = con.execute('select * from users')
#     for row in rs:
#         print(row)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)

    uid = Column(Integer, ForeignKey('user.id', ondelete = 'CASCADE')) #默认就是restrict



Base.metadata.drop_all()
Base.metadata.create_all()

u = User(username='joe')
session.add(u)
session.commit()

art = Article(title='red', content='...', uid=1)
session.add(art)
session.commit()
