import datetime
from connection import mvintegra
from connection import (dbamv, mvintegra, sysdba)



def registrer_painel():
    connection = connection_mysql()
    cursor = connection.cursor()
    
    insert_painel = "insert into painel (nome_painel, tipo, area, link_painel, filtro_data, link_pai) values(:1, :2, :3, :4, :5, :6)"
    cursor.execute(statement, {"1": nome_dic[''], "2":nome_dic[''], "3":nome_dic[''], "4": nome_dic[''], "5": nome_dic[''], "6":nome_dic[''] })

    connection.commit()
    
def registrer_historico(id_painel):
    connection = connection_mysql()
    cursor2 = connection.cursor2()
    
    insert_historico = "insert into historico( user, data_hora, link, idpainel) values(:1, :2, :3, :4)"
    cursor2.execute(statment, {"1": nome_dic[''], "2":nome_dic[''], "3":nome_dic[''], "4": nome_dic['']})
    connection.commit()
    
def registrer_acesso(id_painel):
    connection = connection_mysql()
    cursor3 = connection.cursor3()
    
    insert_acesso = "insert into acesso(user,ativo,papel,acessocol,idpainel) values (:1, :2, :3, :4, :5)"
    cursor3.execute(statment, {"1": nome_dic[''], "2":nome_dic[''], "3":nome_dic[''], "4": nome_dic['']})
    connection.commit()
    

    
    