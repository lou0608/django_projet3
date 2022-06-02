import pyodbc
import pandas as pd
import numpy as np

# Connexion à la base de données

server = 'sql-mcibusxrm-dev.database.windows.net'
database = 'sqldb-mcibusxrm-dev'
username = 'sql-mcibusxrm-dev'
password = '{pzR28UcutX26GdAJLWm9SXw}'
driver= '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

# Requetes SQL pour récuprer les données

df_Mandat = pd.read_sql("SELECT MandatId, CritereId, DateMandatSignature, DateCompromisSignature FROM dbo.Mandat ", conn)

# envoyer résultat de la requete dans une autre bdd

# connexion a l'autre bdd


import MySQLdb as mdb

mydb = mdb.connect(
    host = "localhost",
    user = "lou6",
    password = "Kaleo.31310",
    database = "loan_status")

# Creation bdd

# requete de migration

# insert ???

# un select
# un insert



