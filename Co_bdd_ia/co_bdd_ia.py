from optparse import Values
import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np
import datetime
import MySQLdb as mdb
import mysql.connector

from mysql.connector import Error

# Objectif : 
# Connexion a la base de données MySql Workench
# Creation requete de récupération de données

# But:
# Récuperer csv de données brutes pour l'entrainement du modèle.

try: 
    conn = mysql.connector.connect(
        host = "localhost",
        user = "lou6",
        password = "Kaleo.31310",
        database = "Aboutissement")
    
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("USE Aboutissement;")
        print("Database Aboutissement is connected")
        
except Error as e:
    print("Error while connecting to Mysql", e)
    
query = """ SELECT mandat.MandatId, SurfaceMin, NombrePiecesEnum, NombreChambresEnum, 
localisation.Departement_LocalisationId, departement.Region_LocalisationId, Localisation_Criteres.LocalisationId,
mandat.StatutProspectMandatClientID as StatutMandat, mandat.TypeDeMission as TypeMission, criteres.TypeBienEnum as TypeBien, TypeProjet,

case criteres.BudgetMaxEuro
	    WHEN criteres.BudgetMaxEuro >= 1000 THEN criteres.BudgetMaxEuro
        WHEN criteres.BudgetMaxEuro < 1000 THEN criteres.BudgetMaxEuro * 1000
        ELSE criteres.BudgetMaxEuro
END AS "BudgetMaxEuro",

localisation.Code as "CodePostal",
localisation.Nom as "Ville",
departement.Nom as 'Departement',
region.Nom as 'Region'
from mandat
-- left JOIN BienMandat on BienMandat.MandatId = mandat.MandatId
INNER JOIN Criteres on Criteres.CritereId = mandat.CritereId
left JOIN Localisation_Criteres ON Localisation_Criteres.CritereId = criteres.CritereId
INNER JOIN localisation ON localisation.LocalisationId = Localisation_Criteres.LocalisationId 
AND localisation.Departement_LocalisationId IS NOT NULL AND localisation.Region_LocalisationId IS NULL
LEFT JOIN Localisation departement ON departement.LocalisationId = localisation.Departement_LocalisationId
LEFT JOIN Localisation region ON region.LocalisationId = departement.Region_LocalisationId
WHERE StatutProspectMandatClientId IN (7, 8, 9) AND SurfaceMin !=0 AND BudgetMaxEuro != 0 """ ; 

result_df = pd.read_sql(query, conn)
print(result_df.head())
result_df.info()

result_df.to_csv('Result_final4_4.csv')
