from flask import Flask
from flask import request, redirect, render_template, session, Blueprint, jsonify
from models import db, User, Model_detail, Model
from forms import RegisterModelForm
import datetime
import requests
from . import api_model as api
import pandas as pd
import h2o
import json

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
    try:
        if request.method == 'GET':
            modelId = request.args.get('modelId', '')
            inputData = request.args.get('inputData', '')
            
            model_info = db.session.query(Model).filter(Model.id == modelId).first()
            model = h2o.load_model("./model/{}/{}".format(model_info.category,model_info.modelname))

            data = json.loads(inputData)
            for key, value in data.items():
                data[key] = [value]
            df = pd.DataFrame(data)
            hf = h2o.H2OFrame(df)
            pred = model.predict(hf)
            ret = h2o.as_list(pred).to_json()
            return jsonify(ret), 201
    except:
        return jsonify(), 404