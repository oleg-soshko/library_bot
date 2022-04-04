from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from os import environ

Base = declarative_base()
DATABASE_URL = environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL.replace('postgres', 'postgresql'))


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    date = Column(String, nullable=False)

    def __init__(self, chat_id, first_name, last_name, username=None, date=None):
        self.chat_id = chat_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.date = date


class Feedback(Base):
    __tablename__ = 'feedbacks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    date = Column(String, nullable=False)

    def __init__(self, chat_id, text, date=None):
        self.chat_id = chat_id
        self.text = text
        self.date = date


class Error(Base):
    __tablename__ = 'errors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, nullable=False)
    text_error = Column(String)
    date = Column(String, nullable=False)

    def __init__(self, chat_id, text_error, date=None):
        self.chat_id = chat_id
        self.text_error = text_error
        self.date = date


class UserAction(Base):
    __tablename__ = 'UserActions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, nullable=False)
    action = Column(String)
    date = Column(String, nullable=False)

    def __init__(self, chat_id, action, date=None):
        self.chat_id = chat_id
        self.action = action
        self.date = date


class Library:
    def add_user(self, chat_id, first_name, last_name, username, date=datetime.now().strftime('%d-%m-%Y %H:%M:%S')):
        Session = sessionmaker(bind=engine)
        session = Session()
        user = User(chat_id, first_name, last_name, username, date)
        session.add(user)
        session.commit()

    def check_user(self, chat_id):
        Session = sessionmaker(bind=engine)
        session = Session()
        check_user_data = session.query(User).filter_by(chat_id=chat_id).first()
        return check_user_data

    def add_feedback(self, chat_id, text, date=datetime.now().strftime('%d-%m-%Y %H:%M:%S')):
        Session = sessionmaker(bind=engine)
        session = Session()
        feedback = Feedback(chat_id, text, date)
        session.add(feedback)
        session.commit()

    def add_error(self, chat_id, text_error, date=datetime.now().strftime('%d-%m-%Y %H:%M:%S')):
        Session = sessionmaker(bind=engine)
        session = Session()
        error = Error(chat_id, text_error, date)
        session.add(error)
        session.commit()

    def add_action(self, chat_id, action, date=datetime.now().strftime('%d-%m-%Y %H:%M:%S')):
        Session = sessionmaker(bind=engine)
        session = Session()
        user_action = UserAction(chat_id, action, date)
        session.add(user_action)
        session.commit()


Base.metadata.create_all(engine)
