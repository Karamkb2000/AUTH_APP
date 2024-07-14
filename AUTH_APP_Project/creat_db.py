from database.database import Base,engine
from models import models


print("Creating database ....")
print (engine)
Base.metadata.create_all(engine)
print ("test")