from flask import render_template, Blueprint, url_for, request, redirect
#from app.models.form import Login_user_Painel
 
main = Blueprint('main', __name__)
 
@main.route("/")
def index():
    return render_template('index.html')
@main.route('/', methods=['POST'])
def index_post():
    nome_user_mv = request.form.get('nome_login')
    senha        = request.form.get('senha_login')
    return redirect(url_for('main.login'))

#enddef


@main.route('/login')
def login():
    return render_template('login.html')   
@main.route('/login', methods=['POST'])
def login_post():
    nome_user_mv = request.form.get('nome_login')
    senha        = request.form.get('senha_login')
    return redirect(url_for('main.login'))

#enddef   


@main.route('/signup')
def signup():
    #form = Login_user_Painel()
    return render_template('signup.html')
@main.route('/signup', methods=['POST'])
def signup_post():
    user_name_mv = request.form.get('nome_cad')
    email        = request.form.get('email_cad')
    senha        = request.form.get('senha_cad')
    print(email,user_name_mv,senha)
    
    return redirect(url_for('main.login'))
#enddef'''