from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class Login_user_Painel(FlaskForm):
    email = StringField("email")
    password = PasswordField("password")
    user_name_MV = StringField("user_mv")
    remember_me = BooleanField('remember_me')