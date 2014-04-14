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
    img_path Column(String)
    
    def __init__(self, name, img_path):
	""""""
		name = self.name
		img_path = self.img_path
	
	self.name = name
#######################################################################

Base.metadata.create_all(engine)
