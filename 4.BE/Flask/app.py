import os
from flask import Flask
from flask import request, redirect, render_template, session
from models import db, User, Subscribe_list, Model_detail, Model, Engineer
from forms import RegisterForm, LoginForm
from loginApi import api_l as loginApi
from modelApi import api_m as modelApi
from tradeApi import api_t as tradeApi

app = Flask(__name__)
app.register_blueprint(loginApi, url_prefix='/loginApi')
app.register_blueprint(modelApi, url_prefix='/modelApi')
app.register_blueprint(tradeApi, url_prefix='/tradeApi')


@app.route('/', methods=['GET'])
def check_db():
    user_data = db.session.query(User).all()
    engine_data = db.session.query(Engineer).all()
    sess_id = session.get('userid', None)
    ret = '현재 접속중인 ID : ' + str(sess_id) + '   /   전체 회원 정보 : '
    for user_iter in user_data:
        ret += 'user : ' + str(user_iter.id) + ' -> ' + \
            str(user_iter.userid) + '   /   '
    for engine_iter in engine_data:
        ret += 'engineer : ' + str(engine_iter.id) + \
            ' -> ' + str(engine_iter.userid) + '    /   '
    return ret


basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

db.init_app(app)
db.app = app
db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
