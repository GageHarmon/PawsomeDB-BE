from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from services import db

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    serialize_only = ('id', 'username', 'email', 'password', 'pets')
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)