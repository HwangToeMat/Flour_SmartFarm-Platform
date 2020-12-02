from flask import Flask
from flask import request, redirect, render_template, session, Blueprint, jsonify
from models import db, User, Engineer
from forms import RegisterForm, LoginForm
import datetime
import requests
from . import api_l as api


@api.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['userid'] = form.data.get('userid')

        return redirect('/')

    return render_template('login.html', form=form)


@api.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    return redirect('/')

@api.route('/session', methods=['GET'])
def getSession():
    sess = session['userid']
    return jsonify(sess)

@api.route('/register/user', methods=['GET', 'POST'])
def registerUser():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        user.userid = form.data.get('userid')
        user.name = form.data.get('name')
        user.password = form.data.get('password')

        db.session.add(user)
        db.session.commit()

        return redirect('/')

    return render_template('registerUser.html', form=form)


@api.route('/register/engineer', methods=['GET', 'POST'])
def registerEngineer():
    form = RegisterForm()
    if form.validate_on_submit():
        user = Engineer()
        user.userid = form.data.get('userid')
        user.name = form.data.get('name')
        user.password = form.data.get('password')

        db.session.add(user)
        db.session.commit()

        return redirect('/')

    return render_template('registerEngineer.html', form=form)
