from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(12))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    register_at = db.Column(db.DateTime, server_default=db.func.now())
    subscribe_list = db.relationship(
        'Subscribe_list', backref='user', lazy=True)


class Subscribe_list(db.Model):
    __tablename__ = 'subscribe_list'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subscribe_type = db.Column(db.String(50))
    payment_type = db.Column(db.String(50))
    total_price = db.Column(db.Integer)
    total_quantity = db.Column(db.Integer)
    status = db.Column(db.String(20))
    subscribe_list = db.relationship(
        'Model_detail', backref='subscribe_list', lazy=True)

    # @property
    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'user_id': self.user_id,
    #         'total_price': self.title,
    #         'fcuser': self.fcuser.userid,
    #         'tstamp': self.tstamp
    #     }


class Model_detail(db.Model):
    __tablename__ = 'model_detail'

    id = db.Column(db.Integer, primary_key=True)
    subscribe_list_id = db.Column(db.Integer, db.ForeignKey(
        'subscribe_list.id'), nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=False)
    register_at = db.Column(db.DateTime)
    unregister_at = db.Column(db.DateTime)
    model = db.relationship(
        'Model', backref='model_detail', lazy=True)

    # @property
    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'title': self.title,
    #         'fcuser': self.fcuser.userid,
    #         'tstamp': self.tstamp
    #     }


class Model(db.Model):
    __tablename__ = 'model'

    id = db.Column(db.Integer, primary_key=True)
    engineer_id = db.Column(db.Integer, db.ForeignKey(
        'engineer.id'), nullable=False)
    modelname = db.Column(db.String(30))
    version = db.Column(db.String(100))
    content = db.Column(db.String(100))
    price = db.Column(db.Integer)
    register_at = db.Column(db.DateTime, server_default=db.func.now())


class Engineer(db.Model):
    __tablename__ = 'engineer'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(12))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    register_at = db.Column(db.DateTime, server_default=db.func.now())
    model = db.relationship(
        'Model', backref='engineer', lazy=True)
