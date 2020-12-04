import os
from flask import Flask
from flask import request, redirect, render_template, session
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS
from models import db, User, Model_detail, Model, Engineer
from forms import RegisterForm, LoginForm
from loginApi import api_l as loginApi
from marketApi import api_m as marketApi
from modelApi import api_model as modelApi
import h2o

app = Flask(__name__)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
CORS(app)
app.register_blueprint(loginApi, url_prefix='/loginApi')
app.register_blueprint(marketApi, url_prefix='/marketApi')
app.register_blueprint(modelApi, url_prefix='/modelApi')


@app.route('/', methods=['GET'])
def check_db():
    user_data = db.session.query(User).all()
    engine_data = db.session.query(Engineer).all()
    model_data = db.session.query(Model).all()
    model_detail_data = db.session.query(Model_detail).all()
    sess_id = session.get('userid', None)
    ret = '현재 접속중인 ID : ' + str(sess_id) + '   /   전체 회원 정보 : '
    for user_iter in user_data:
        ret += 'user : ' + str(user_iter.id) + ' -> ' + \
            str(user_iter.userid) + '   /   '
    for engine_iter in engine_data:
        ret += 'engineer : ' + str(engine_iter.id) + \
            ' -> ' + str(engine_iter.userid) + '    /   '
    return ret
    
@manager.command
def run():
    app.run(host='127.0.0.1', port=5000, debug=True)

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'
app.config['JSON_AS_ASCII'] = False

db.init_app(app)
db.app = app
db.create_all()

if __name__ == '__main__':
    # manager.run()
    h2o.init(ip="127.0.0.1", max_mem_size_GB = 200, nthreads = 10)
    app.run(host='0.0.0.0', port=5000, debug=True)
