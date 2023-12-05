import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_NAME = os.getenv('DB_NAME') #' proyectoFinalDBProgram'
DB_URL = 'sqlite:///db/{db_name}.db'.format(db_name=DB_NAME)
DB_ECHO = True if os.getenv('DB_ECHO') else False

engine = create_engine(DB_URL, echo=DB_ECHO)
Session = sessionmaker(bind=engine)
