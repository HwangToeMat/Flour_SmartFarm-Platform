from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(12))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    model_detail = db.relationship(
        'Model_detail', backref='user', lazy=True)


class Model_detail(db.Model):
    __tablename__ = 'model_detail'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=False)
    model = db.relationship(
        'Model', backref='model_detail', lazy=True)


class Model(db.Model):
    __tablename__ = 'model'

    id = db.Column(db.Integer, primary_key=True)
    engineer_id = db.Column(db.Integer, db.ForeignKey(
        'engineer.id'), nullable=False)
    modelname = db.Column(db.String(30))
    version = db.Column(db.String(100))
    content = db.Column(db.String(100))
    category = db.Column(db.String(30))
    price = db.Column(db.String(30))


class Engineer(db.Model):
    __tablename__ = 'engineer'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(12))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    model = db.relationship(
        'Model', backref='engineer', lazy=True)
