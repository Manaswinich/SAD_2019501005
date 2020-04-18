from datetime import datetime
from sqlalchemy import Column, String, Integer
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os

Base = declarative_base()


class User(Base):
    __tablename__ = 'students'
    # fname = Column(String(50))
    # lname = Column(String(50))
    # gender = Column(String(50))
    # email = Column(String(120))
    usr = Column(String(50), primary_key=True)
    password = Column(String(20))
    time = Column(TIMESTAMP, default=datetime.now(), nullable=False)


    # def __init__(usr, pwd):
    #     self.usr = usr
    #     self.pwd = pwd
    # self.time = time

    def __repr__(self):
        return '<User %r is added.>' % (self.usr)


# class Book(Base):
#     __tablename__ = 'book'
#     isbn = Column(String(50), primary_key=True)
#     name = Column(String(50))
#     title = Column(String(50))
#     year = Column(Integer)

#     def __init__(self, isbn, title, author, year):
#         self.isbn = isbn
#         self.title = title
#         self.author = author
#         self.year = year


# class admin(Base):
#     __tablename__ = 'admin'
#     # fname = Column(String(50))
#     # lname = Column(String(50))
#     # gender = Column(String(50))
#     # email = Column(String(120))
#     usr = Column(String(50), primary_key=True)
#     pwd = Column(String(20))
#     time = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)

#     def __init__(usr, pwd):
#         self.usr = usr
#         self.pwd = pwd

#     def __repr__(self):
#         return '<Admin %r is added.' % (self.usr)


# class review(Base):
#     __tablename__ = 'admin'
#     usr = Column(String(50), primary_key=True)
#     isbn = Column(String(50), primary_key=True)

#     def __init__(usr, isbn):
#         self.usr = usr
#         self.isbn = isbn

#     def __repr__(self):
#         return '<User %r has reviewed the %r book.' % (self.usr, self.isbn)
engine = create_engine(os.getenv("DATABASE_URL"))
Base.metadata.create_all(engine)
