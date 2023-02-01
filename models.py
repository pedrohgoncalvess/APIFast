from sqlalchemy import Column,Integer,String
from database import Base

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer,primary_key=True)
    task = Column(String(256))


class Lead(Base):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key = True)
    lead_name = Column(String(100))
    lead = Column(String(500))