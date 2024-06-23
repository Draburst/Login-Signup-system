from sqlalchemy import Column, Boolean, Sequence, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship, backref, declarative_base
engine = create_engine("sqlite:///./app.db?check_same_thread=False")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String, unique=True)
    password = Column(String(50))
    is_admin = Column(Boolean, default=False)

    transactions = relationship('Transaction', backref='user', lazy=True)

    def __repr__(self):
        return f"<User(username='{self.username}', is_admin={self.is_admin})>"

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    balance = Column(Integer)
    amount = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    category = Column(String)

Base.metadata.create_all(engine)