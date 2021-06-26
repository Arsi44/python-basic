from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

config_dotenv = dotenv_values(".env")

# need to create database before
engine = create_engine('postgresql+psycopg2://postgres:Hrieleght2@localhost/example')
# engine = create_engine('sqlite:///example33.db')
Session = sessionmaker(bind=engine)
my_session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String, unique=True)
    children_bind_post = relationship("Post", back_populates="parent_bind_user")

    def __repr__(self):
        return "<User(name='%s', username='%s', email='%s')>" % (
            self.name, self.username, self.email)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    users_id = Column(Integer, ForeignKey('users.id'))
    parent_bind_user = relationship("User", back_populates="children_bind_post")

    children_bind_comment = relationship("Comment", back_populates="parent_bind_post")

    def __repr__(self):
        return "<Post(users_id='%s', title='%s')>" % (
            self.users_id, self.title)


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    text = Column(String)  # "name"
    post_id = Column(Integer, ForeignKey('posts.id'))
    sender_email = Column(String, ForeignKey('users.email'))
    parent_bind_post = relationship("User", back_populates="children_bind_comment")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)
