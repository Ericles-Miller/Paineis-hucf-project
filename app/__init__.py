from flask import Flask
#from Flask_sqlalchemy import SQLAlchemy
#import mysql.connector
#import json
#from connection.py import connection_mysql

def create_app():
    app = Flask(__name__)
    
    app.secret_key = 'adlo895020'
      
    from .default import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    #app.register_blueprint(auth_blueprint)
    
    return app 
    
'''
app.congig['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHAMY_DATABASE_URI'] = database

db = SQLAlchemy(app)

class Acesso(db.Model):
    id_acesso = db.column('id', db.Interger, primary_key = True, autoincrement= True, notnull = true)
    user      = db.column(db.String(50))
    ativo     = db.column(db.Integer)
    papel     = db.column(db.string(50))
    acessocol = db.column(db.string(50))
    painel_idpainel = db.column('id_painel', db.Integer, foreng_key = True, notnull = True)
    
    
    def __init__(self,user,papel,ativo,acessocol,painel_idpainel):
        self.nome_user_mv = user
        self.user_ativo   = ativo
        self.papel_user   = papel
        self.acessocol    = acessocol
        self.id_painel    = painel_idpainel'''