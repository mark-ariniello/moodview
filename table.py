import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Photo
 
engine = create_engine('sqlite:///photos.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create a Photo(name, photo)
p1 = Photo("Beach", "/img/Beach")
p2 = Photo("Sunset", "/img/Sunset")
p3 = Photo("Mountains", "/img/Mountains")
p4 = Photo("Ocean", "/img/Ocean")
p5 = Photo("Stars", "/img/Stars")
p6 = Photo("River", "/img/River")
 
# Add the record to the session object
session.add_all([p1,p2,p3,p4,p5,p6])
# commit the record the database
session.commit()
 
