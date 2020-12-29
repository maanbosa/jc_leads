from db import db
from datetime import datetime

class LeadModel(db.Model):
    # to create table across SQLAlchemy
    __tablename__ = 'leads'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    id_number = db.Column(db.String(15))
    email = db.Column(db.String(80))
    mobile = db.Column(db.String(20))
    archived = db.Column(db.Boolean)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # to create object
    def __init__(self, name, id_number, email, mobile, archived=False):
        self.name = name
        self.id_number = id_number
        self.email = email
        self.mobile = mobile
        self.archived = archived

    # convert default tuple in json
    def json(self):
        return {
            'name': self.name,
            'id_number': self.id_number,
            'email': self.email,
            'mobile': self.mobile,
            'archived': self.archived
        }

    # convert default tuple in json
    def json_from_db(self):
        return {
            'id': self.id,
            'name': self.name,
            'id_number': self.id_number,
            'email': self.email,
            'mobile': self.mobile,
            'archived': self.archived,
            'created': str(self.created),
            'updated': str(self.updated)
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete()
        db.session.commit()


    
    




