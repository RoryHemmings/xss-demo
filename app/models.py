from app import db
from datetime import datetime

import uuid

# one to many model
class WebPage(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.String(36), primary_key=True)
    messages = db.relationship("Message", backref='page', uselist=True)

    def __init__(self):
        new_id = str(uuid.uuid4())
        print(new_id)
        self.id = new_id


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    parent = db.Column(db.String(), db.ForeignKey("pages.id"), nullable=False)    


    def __init__(self, content, author):
        self.id = str(uuid.uuid4())
        self.content = content
        self.author = author
        self.date = datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
