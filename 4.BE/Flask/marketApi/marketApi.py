from flask import Flask
from flask import request, redirect, render_template, session, Blueprint, jsonify
from models import db, User, Model_detail, Model
from forms import RegisterForm, LoginForm
import datetime
import requests
from . import api_m as api


@api.route('/', methods=['GET', 'POST'])
def market():
    if request.method == 'POST':
        model_detail = Model_detail()
        data = request.get_json()
        sess_id = data['userid']
        modelid = data['modelId']
        user_info = db.session.query(User).filter(User.userid == sess_id).first()
        if user_info != None:
            model_detail.user_id = user_info.id
            model_detail.model_id = int(modelid)
            db.session.add(model_detail)
            db.session.commit()
        else:
            return jsonify(), 404
        return jsonify(), 201
    elif request.method == 'GET':
        model_data = db.session.query(Model).all() 
        ret = []
        for model_iter in model_data:
            row = {'id' : model_iter.id, 'modelname' : model_iter.modelname, 'version' : model_iter.version, 'content' : model_iter.content, 'price' : model_iter.price, 'category' : model_iter.category}
            ret.append(row)
        return jsonify(ret)

