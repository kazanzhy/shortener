from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, SmallInteger
from . import engine

BaseModel = declarative_base()

class Link(BaseModel):
    '''
    Model for table with links and short cone
    '''
    __tablename__ = 'links'

    def __init__(self, code, link):
        self.code = code
        self.link = link
        self.redirects = 0

    id = Column(Integer, primary_key=True)
    code = Column(String(16), index = True, unique = True)
    link = Column(String(128), index = True, unique = True)
    redirects = Column(Integer)

    def __repr__(self):
        return '<Link ({}, {})>'.format(self.code, self.link)


class User(BaseModel):
    '''
    Model for users
    '''
    __tablename__ = 'users'

    def __init__(self, username, email, password):
        self.username = name
        self.email = email
        self.password = password

    id = Column(Integer, primary_key = True)
    username = Column(String(64), index = True, unique = True)
    email = Column(String(128), index = True, unique = True)
    role = Column(SmallInteger, default = 1)

    def __repr__(self):
        return '<User ({})>'.format(self.nickname)


BaseModel.metadata.create_all(engine)




















