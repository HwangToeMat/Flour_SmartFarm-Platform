from flask import Flask
from flask import request, redirect, render_template, session, Blueprint, jsonify
from models import db, User, Model_detail, Model
from forms import RegisterModelForm
import datetime
import requests
from . import api_model as api

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

        return redirect('/')

    return render_template('registerModel.html', form=form)


@api.route('/mymodel', methods=['POST'])
def mymodel():
    if request.method == 'POST':
        model_detail = Model_detail()
        data = request.get_json()
        sess_id = data['userid']
        user_info = db.session.query(User).filter(User.userid == sess_id).first()
        if user_info != None:
            ret = set()
            userId = user_info.id
            user_data = db.session.query(Model_detail).filter(Model_detail.user_id == userId).all()
            for user_iter in user_data:
                md_id = user_iter.model_id
                ret.add(md_id)
        else:
            return jsonify(), 404
        print(ret)
        return jsonify(ret), 201