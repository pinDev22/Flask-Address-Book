from app import db
from werkzeug.security import generate_password_hash
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs.get('password'))
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return f"<User {self.id}| {self.username}>"

    class Address(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String, nullable=False)
        last_name = db.Column(db.String, nullable=False)
        phone_number = db.Column(db.String, nullable=False, unique=True)
        address = db.Column(db.String, nullable=False, unique=True)
        date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        user_id = db.Column(db.Integer, foreign_key=True)

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            db.session.add(self)
            db.session.commit()
        
        def __repr__(self):
            return f"<Address {self.id}| {self.address}>"

