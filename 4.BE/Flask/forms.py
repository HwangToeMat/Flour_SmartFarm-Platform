from models import User, Engineer
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    userid = StringField('userid', validators=[DataRequired()])
    name = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo(
        'repassword', message='Passwords must match')])
    repassword = PasswordField('repassword', validators=[DataRequired()])


class LoginForm(FlaskForm):

    class UserPassword(object):
        def __init__(self, message=None):
            self.message = message

        def __call__(self, form, field):
            userid = form['userid'].data
            password = field.data

            user = User.query.filter_by(userid=userid).first()

            if user != None:
                if user.password != password:
                    raise ValueError('Wrong password')
            else:
                user = Engineer.query.filter_by(userid=userid).first()
                if user != None:
                    if user.password != password:
                        raise ValueError('Wrong password')
                else:
                    raise ValueError('Wrong ID')

    userid = StringField('userid', validators=[DataRequired()])
    password = PasswordField('password', validators=[
                             DataRequired(), UserPassword()])
