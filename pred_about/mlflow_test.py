import  os
import warnings
import sys

import mlflow
from  mlflow  import log_metric, log_param, log_artifact 
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import lightgbm as lgb
from sklearn.metrics import accuracy_score, precision_score
from sklearn.metrics import recall_score
import pandas as pd
import numpy as np

# librairie d'envoie mail, connexion sécurisée
import smtplib, ssl


# Data
df = pd.read_csv('Result_final_3.csv', sep = ",")
df = df.drop("Unnamed: 0", axis = 1)
df.drop(["MandatId", "BienMandatId","CritereId","Statut","StatutMandat","DateCreation", "DescriptionBien_DateOffreAcceptee","Origine_DateCollecte", "Departement_LocalisationId", "Region_LocalisationId", "LocalisationId"], axis = 1, inplace = True)
X =df.drop(["Succes", "Ville", "Departement", "Region"], axis = 1)
y=df["Succes"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Fonction metrics
def eval_metrics(y_test, y_pred):
    acc = accuracy_score(y_test, y_pred)
    pre = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    return acc, pre, rec


# fonction alerte    
def send_alert(model):
    smtp_server = 'smtp.gmail.com' 
    port = 465 
    destinateur = 'loudoussiet@gmail.com' 
    password = 'kaleo31310' 
    destinataire = 'loudoussiet@gmail.com'   
    password = "kaleo31310"
    message = """\
    Subject: Alert Accuracy too low
    This model {} is not efficient enough
    This message is sent from python.""".format(model)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(destinateur, password)
        server.sendmail(destinateur, destinataire, message) 
    print("alert send !") 

if __name__ == "__main__":

    model1 = lgb.LGBMClassifier()

def train(model):
    alert_accuracy = False      
    warnings.filterwarnings("ignore")
    
    with mlflow.start_run(run_name="Product Classification Experiment") as run:
        mlflow.lightgbm.autolog()
        
        num_trees = 250
        max_trees_depth = 5
        
        clf = lgb.LGBMClassifier()
        model = clf.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy_model = accuracy_score(y_test, y_pred)
        mlflow.sklearn.log_model(model, "model")
        
        #print(model.booster_)
        #print(model.feature_importances_)
        #print(model.objective_)
        #print(model.best_score_)
        #print(model.best_iteration_)
        
        (acc, pre, rec) = eval_metrics(y_test, y_pred)
        print("  Acc: %s" % acc)
        print("  Pre: %s" % pre)
        print("  Rec: %s" % rec)
        
        #mlflow.log_param(boosting_type, "goos")
        
        mlflow.log_param("num_trees", num_trees)
        mlflow.log_param("max_trees_depth", max_trees_depth)
        
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("precision", pre)
        mlflow.log_metric("recall", rec)
        #data.to_csv("Artifact.csv", encding = "utf-8", index = False)
        
        
        if acc < 0.9:
            alert_accuracy = True
            mlflow.log_param("alert low score", alert_accuracy) # add alert in MLFlow
            mlflow.end_run()
            send_alert(model)
        else:
            alert_accuracy = False
            mlflow.log_param("alert low score", alert_accuracy)
        
            #mlflow.log_artifact("/Artifact.csv")
           
        mlflow.sklearn.log_model(model, "model")
        
train(model1)
    

