from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"  # optional, sets explicit table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
