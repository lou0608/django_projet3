from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.response import Response

import joblib
import pandas as pd
from sqlalchemy import values

from prediction.query_sql.read1 import query1
from .forms import RechercheForm

from .models import ChasseursInscription, Form_Register


def Signup(request):
    if request.method == 'POST':
        Nom = request.POST.get("Nom")
        Prenom = request.POST.get("Prenom")
        Mot_de_passe = request.POST.get("Mot_de_passe")
        Mot_de_passe2 = request.POST.get("Mot_de_passe2")
        Email = request.POST.get("Email")
        if Mot_de_passe!= Mot_de_passe2:
            return render(request, "prediction/signup.html", {"error": "Les mots de passe ne correspondent pas"})
        if Mot_de_passe == Mot_de_passe2:
            ChasseursInscription.objects.create(Nom = Nom, Prenom = Prenom, Mot_de_passe = Mot_de_passe,
                                                Mot_de_passe2 = Mot_de_passe2, Email = Email)
            return redirect("/auth/")
        
    return render(request, 'prediction/signup.html')


def Auth(request):
    if request.method == 'POST':
        Nom = request.POST.get("Nom")
        Prenom = request.POST.get("Prenom")
        Mot_de_passe = request.POST.get("Mot_de_passe")
        if ChasseursInscription.objects.filter(
            Nom__icontains = Nom,
            Prenom__icontains = Prenom,
            Mot_de_passe__icontains = Mot_de_passe):
            return redirect ("/home/")
        
    return render(request, 'prediction/auth.html')
                         
            
# fonction Formulaire
def Recherche(request):
    if request.method == 'POST':
        form = RechercheForm(request.POST)
        if form.is_valid():
            model = load_model()
            pred, pred_probability, pred_proba_positif = run_model(model, form.cleaned_data)
            Form_Register.objects.create(TypeMission = form.cleaned_data.get("TypeMission"),
                                         TypeBien = form.cleaned_data.get("TypeBien"),
                                         TypeProjet = form.cleaned_data.get('TypeProjet'),
                                         CodePostal = form.cleaned_data.get("CodePostal"), 
                                         Budget = form.cleaned_data.get("Budget"),
                                         NombrePieces = form.cleaned_data.get("NombrePieces"),
                                         NombreChambres = form.cleaned_data.get("NombreChambres"),
                                         Surface = form.cleaned_data.get("Surface"),
                                         Prediction = pred)
            plot_div, plot_div1, plot_div2, y = query1(request)
            return render(request, 'prediction/index.html', context= {'form':form, 'pred':pred, 'plot_div': plot_div, 'plot_div1':plot_div1, 'plot_div2':plot_div2, "pred_probability": pred_probability, "y" : y, "pred_proba_positif" : pred_proba_positif})

    else:
        pred = []
        form = RechercheForm()
        return render(request, 'prediction/index.html',{'form':form})

# Read Model
def load_model():
    model = joblib.load(r"C:\Users\Lou Doussiet\Downloads\api_rest_django\prediction\LGBMClassifier.pkl")
    return model

# Prediction    
def run_model(model, data):
    df = pd.DataFrame([data])
    print(df)
    df = df[["Surface", "NombrePieces", "NombreChambres", "TypeMission", "TypeBien", "TypeProjet", "Budget", "CodePostal"]]
    #df.reindex(columns=["Surface", "NombrePieces", "NombreChambres", "TypeMission", "TypeBien", "TypeProjet", "Budget", "CodePostal"])
    #print(df.info())
    df = df.rename(columns={"Surface":"f0", "NombrePieces": "f1", "NombreChambres":"f2", "TypeMission": "f3","TypeBien": "f4","TypeProjet": "f5", "Budget": "f6", "CodePostal": "f7"})
    df['f1'] = df['f1'].astype(int)
    df['f2'] = df['f2'].astype(int)
    df['f3'] = df['f3'].astype(int)
    df['f4'] = df['f4'].astype(int)
    df['f5'] = df['f5'].astype(int)
    model = model 
    cols = list(df.columns.values)
    print(cols)
    pred = pd.Series(model.predict(df[cols]))[0]
    pred_probability = model.predict_proba(df)
    print(pred_probability)
    pred_probability = model.predict_proba(df)[:,0] * 100
    print(pred_probability)
    pred_probability = float(pred_probability)
    #pred_probability = int(pred_probability)
    pred_probability = round(pred_probability, 2)
    pred_proba_positif = model.predict_proba(df)
    pred_proba_positif = model.predict_proba(df)[:,1] *100
    pred_proba_positif = float(pred_proba_positif)
    pred_proba_positif = round(pred_proba_positif, 2)
    #round(pred_proba_positif, 2)
    #pred_proba_positif = int(pred_proba_positif)
    print(pred)
    print(pred_proba_positif)
    print(pred_probability)
    return pred, pred_probability, pred_proba_positif





from rest_framework import viewsets
from .models import Bienmandat, Criteres, Localisation, Mandat, Form_Register, Localisation_Criteres
#, Chasseurs

from .serializers import BienMandatSerializer, CriteresSerializer, LocalisationSerializer
from .serializers import MandatSerializer, Form_RegisterSerializer, Localisation_criteresSerializer
#, ChasseursSerializer

from prediction import forms, serializers
from prediction.forms import RechercheForm

class BienMandatViewSet(viewsets.ModelViewSet):
    serializer_class = BienMandatSerializer
    queryset = Bienmandat.objects.all()
    
    def list(self, request, pk = None):
        queryset = Bienmandat.objects.all()
        serializer = BienMandatSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = BienMandat.objects.all()
        BienMandat = get_object_or_404(queryset, pk=pk)
        serializer = BienMandatSerializer(BienMandat)
        return Response(serializer.data)
      
    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
    
class CriteresViewSet(viewsets.ModelViewSet):
    serializer_class = CriteresSerializer
    queryset = Criteres.objects.all()
    
class LocalisationViewSet(viewsets.ModelViewSet):
    serializer_class = LocalisationSerializer
    queryset =Localisation.objects.all()

class Localisation_criteresViewSet(viewsets.ModelViewSet):
    serializer_class =Localisation_criteresSerializer
    queryset = Localisation_Criteres.objects.all()

class MandatViewSet(viewsets.ModelViewSet):
    serializer_class = MandatSerializer
    queryset = Mandat.objects.all()
       
class Form_RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = Form_RegisterSerializer
    queryset = Form_Register.objects.all()  
    
# class ChasseursViewSet(viewsets.ModelViewSet):
#     serializer_class = ChasseursSerializer
#     queryset = Chasseurs.objects.all() 

