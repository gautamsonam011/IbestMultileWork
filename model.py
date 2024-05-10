# from db import Base
from sqlalchemy import Column,Integer,String
from db import Base as Basex
from sqlalchemy.ext.declarative import declared_attr

class Base(Basex):
   __abstract__= True
   
   @declared_attr
   def __tablename__(cls):
      return cls.__name__.lower()

class Books(Base):
   # __tablename__ = 'books'  
   id = Column(Integer,primary_key=True, index = True)
   name = Column(String(50))
   author = Column(String(50))
   publisher = Column(String(50))