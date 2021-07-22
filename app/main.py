'''from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import *
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from . import db
from .models import User
import subprocess

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return render_template('home.html', name=current_user.name)




@main.route('/login')
@login_required
def login_users():
    return render_template('login.html', name = current_user.name, email=current_user.email)

def login_users_post():
    login = request.form.get('ad_user_gogin') # verificar essa linha 
    try:
        print("FDFDFDFDFDFDF")                  # RETIRAR DEPOIS

    except: 
        print('Usuário inválido ou inexistente!')




@main.route('/logout.html')
@login_required
def logout():
    return render_template('logout.html')'''