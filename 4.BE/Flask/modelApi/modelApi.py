from flask import Flask
from flask import request, redirect, render_template, session, Blueprint, jsonify
from models import db, User, Model_detail, Model
from forms import RegisterModelForm
import datetime
import requests
from . import api_model as api
import h2o

@api.route('/register/model', methods=['GET', 'POST'])
def registerModel():
    form = RegisterModelForm()
    if form.validate_on_submit():
        model = Model()
        model.engineer_id = session['userid']
        model.modelname  = form.data.get('modelname')
        model.version  = form.data.get('version')
        model.content  = form.data.get('content')
        model.category  = form.data.get('category')
        model.price   = form.data.get('price')

        db.session.add(model)
        db.session.commit()

        return redirect('http://192.168.1.10:3000/market')

    return render_template('registerModel.html', form=form)


@api.route('/mymodel', methods=['GET'])
def mymodel():
    if request.method == 'GET':
        model_detail = Model_detail()
        sess_id = request.args.get('userid', '')
        user_info = db.session.query(User).filter(User.userid == sess_id).first()
        if user_info != None:
            model_json = []
            ret = set()
            userId = user_info.id
            user_data = db.session.query(Model_detail).filter(Model_detail.user_id == userId).all()
            for user_iter in user_data:
                md_id = user_iter.model_id
                ret.add(md_id)
            ret_lst = list(ret)
            for ret_iter in ret_lst:
                model_iter = db.session.query(Model).filter(Model.id == ret_iter).first()
                row = {'modelname' : model_iter.modelname, 'version' : model_iter.version, 'category' : model_iter.category}
                model_json.append(row)
            return jsonify(model_json), 201
        else:
            return jsonify(), 404

@api.route('/h2omodel', methods=['GET'])
def h2omodel():
    if request.method == 'GET':
        data = request.get_json()
        model = h2o.load_model("./model/total/XGBoost_grid__1_AutoML_PH")
        df = pd.read_csv("qy_grw.csv", index_col=0)
        hf = h2o.H2OFrame(df.loc[])
        pred = model.predict(hf)
        result = df.to_json(orient="split")
        parsed = json.loads(result)
        json.dumps(parsed, indent=4)