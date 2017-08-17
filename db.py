# taken from http://www.rmunn.com/sqlalchemy-tutorial/tutorial.html
# sqlite connection for nutbot

import sqlite3
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///.db')

Base = declarative_base() 

# create session
Session = sessionmaker(bind=engine)
session = Session()



# class for table
class Card(Base):
    __tablename__ = 'cards'
    
    id = Column(Integer, primary_key = True)
    name = Column(String)
    desc = Column(String) #description
    
    # optional
    def __repr__(self):
        return "<Card: name=%s, descritpion=%s>" % \
                self.name, self.desc,

# what is this for?
Base.metadata.create_all(engine)

def add_card(dct):
    """
       adds dict card to the database
       keys in param dict must match instance vars in Card
    """
    card = Card(**dct) # unfolds dict
    session.add(card)
    session.commit()


for instance in session.query(Card).order_by(Card.id):
    print(instance.name, instance.desc)
    



