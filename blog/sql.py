from sqlalchemy import create_engine, Column, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'db1'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URI)
con = engine.connect()
result = con.execute('select 1')
print(result.fetchone())


Base = declarative_base(DB_URI)


class Person(Base):
    __tablename__ = 'person'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(50))
    

Base.metadata.create_all()

