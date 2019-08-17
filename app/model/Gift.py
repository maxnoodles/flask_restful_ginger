from flask import current_app
from sqlalchemy import Column, Integer, String, Boolean, \
    Float, ForeignKey, SmallInteger, desc, func
from sqlalchemy.orm import relationship

from app.model.base import Base


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    # 是否被赠送
    launched = Column(Boolean, default=False)