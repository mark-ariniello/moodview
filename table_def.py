from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///photos.db', echo=True)
Base = declarative_base()

#######################################################################
class Photo(Base):
    """"""
    __tablename__ = "Photos"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __init__(self, name):
	""""""
	
	self.name = name
#######################################################################

Base.metadata.create_all(engine)
