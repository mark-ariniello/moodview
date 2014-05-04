import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Photo
 
engine = create_engine('sqlite:///Photos.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create a Photo(name, photo)
p1 = Photo("Beach", "/img/Beach", 10)
p2 = Photo("Sunset", "/img/Sunset", 9)
p3 = Photo("Mountains", "/img/Mountains", 8)
p4 = Photo("Ocean", "/img/Ocean", 7)
p5 = Photo("Stars", "/img/Stars", 6)
p6 = Photo("River", "/img/River", 5)
 
# Add the record to the session object
session.add_all([p1,p2,p3,p4,p5,p6])
# commit the record the database
session.commit()
 
