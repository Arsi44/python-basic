from sqlalchemy import create_engine, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///example2.db')
Session = sessionmaker(bind=engine)
my_session = Session()
Base = declarative_base()

# Many To Many (bidirectional *-двунаправленная)
association_table = Table('association', Base.metadata,
                          Column('left_id', Integer, ForeignKey('left.id')),
                          Column('right_id', Integer, ForeignKey('right.id'))
                          )


class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship(
        "Child",
        secondary=association_table,
        back_populates="parents")


class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    parents = relationship(
        "Parent",
        secondary=association_table,
        back_populates="children")


Base.metadata.create_all(engine)
