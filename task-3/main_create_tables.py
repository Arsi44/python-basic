from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

config_dotenv = dotenv_values(".env")

# need to create database before
engine = create_engine('postgresql+psycopg2://postgres:Hrieleght2@localhost/example')
# engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    children_bind_post = relationship("Post", back_populates="parent_bind_user")
    bind_from_user = relationship("Comment", back_populates="bind_to_user")

    def __repr__(self):
        return "<User(name='%s', username='%s', email='%s')>" % (
            self.name, self.username, self.email)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'))  # тут мы указываем значение без ссылки

    parent_bind_user = relationship("User", back_populates="children_bind_post")  # а тут как раз ссылка на значение
    children_bind_comment = relationship("Comment", back_populates="parent_bind_post")

    def __repr__(self):
        return "<Post(users_id='%s', title='%s')>" % (
            self.users_id, self.title)


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)  # "name"
    post_id = Column(Integer, ForeignKey('posts.id'))
    sender_email = Column(String, ForeignKey('users.email'))
    parent_bind_post = relationship("Post", back_populates="children_bind_comment")
    bind_to_user = relationship("User", back_populates="bind_from_user")

    def __repr__(self):
        return "<Comment(text='%s')>" % (
            self.text)


def create_user(name: str, username: str, email: str) -> User:
    user = User(name=name, username=username, email=email)
    my_session.add(user)
    my_session.commit()
    return user


def create_post(user_id: int, title: str) -> Post:
    current_user = my_session.query(User).filter_by(id=user_id).first()
    post = Post(title=title, parent_bind_user=current_user)
    my_session.add(post)
    my_session.commit()
    return post


def create_comment(user_id, post_id, text) -> Comment:
    current_user = my_session.query(User).filter_by(id=user_id).first()
    current_post = my_session.query(Post).filter_by(id=post_id).first()
    comment = Comment(text=text, parent_bind_post=current_post, bind_to_user=current_user)
    my_session.add(comment)
    my_session.commit()
    return comment


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    my_session = Session()

    # user = create_user('n', 'un', 'em')
    # post = create_post(user.id, 'title_1')
    # comment = create_comment(user.id, post.id, 'ttttext_1')
