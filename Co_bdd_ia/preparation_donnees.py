import pandas as pd
import numpy as np


# Obejctif :
# Nettoyer les données
# Transfomer les données pour l'entrainement du modèle

#But:  
# Récupérer un csv qui contient les données finales pour l'entrainement du modèle


df = pd.read_csv('Result_final4_4.csv', sep = ",")
#print(df.info())
#print(df.head())

# Nettoyer les données
# Drop value in columns StatutMandat

valeurs = [1, 5, 6, 12]
df = df[df.StatutMandat.isin(valeurs) ==  False ]
#print(df["StatutMandat"].value_counts())

# Features engenering
# Creation de la colonne Succes

conditionlist = [
    (df['StatutMandat'] == 9),
    (df['StatutMandat'] == 7),
    (df['StatutMandat'] == 8)]

choicelist = ['0','1','1']
df['Succes'] = np.select(conditionlist, choicelist, default='Not Specified')
#print(df["Succes"].value_counts())

# Changement du type de la colonne Succes
df["Succes"] = df["Succes"].astype(int)
df["Succes"] = df["Succes"].astype({"Succes": np.dtype("int64")})
#df.info()

# Division pour égalisation du label
df1 = df.loc[df["Succes"] == 0]
#print(df1["Succes"].value_counts())
df2 = df.loc[df["Succes"] == 1]
#print(df2["Succes"].value_counts())
df1 = df1.copy()

# Suppression des valeurs en trop
df1.drop(df1.index[:9306], inplace=True)

# Concatenation des deux dataframes
df = pd.concat([df1, df2], ignore_index = True)

# Verification des valeurs de la colonne Succes
print(df["Succes"].value_counts())

# Données brutes finales pour l'entrainement du modèle
df.to_csv('Result_final_3.csv')
df.head()