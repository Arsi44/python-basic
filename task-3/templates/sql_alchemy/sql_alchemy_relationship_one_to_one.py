from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///example3.db')
Session = sessionmaker(bind=engine)
my_session = Session()
Base = declarative_base()


# One To One (uselist=False!!!!!)
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    children_bind = relationship("Address", back_populates="parent_bind", uselist=False)  # link to child element


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    some_text = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))  # link to parent column
    parent_bind = relationship("User", back_populates="children_bind")  # for bidirectionality


Base.metadata.create_all(engine)