import MySQLdb
import fdb


def connection_mysql():
    db = MySQLdb.connect(
        Host="localhost",    # your Host, usually localhost
        user="root",         # your username
        passwd="root",  # your password
        db="project_painel")  # name of the data base
    

#Conexão com firebird
def sysdba():
    conn = fdb.connect(host="10.10.1.94",database="/opt/firebird/sisinthucf.fdb", user="SYSDBA", password="masterkey")
    return conn