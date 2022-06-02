from django.db import models 
from .forms import RechercheForm

from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.response import Response
from django.db import connection

from prediction.forms import RechercheForm
import pandas as pd

from plotly.offline import plot
import plotly.graph_objs as go

from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://lou6:Kaleo.31310@localhost:3306/aboutissement")
conn = engine.connect()

import logging

# Creation d'un modele a partir du formulaire
# choix:
# - reutilisation du formulaire déjà créer et rempli un model avec le resulat de la fonction de prediciton
# - creer un model de formulaire en dur qui sera rempli avec les données du formulaire grace a l'orm

def pred_bdd(request):
        if request.method == 'POST':
            form = RechercheForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                form.save()
        else :
            form = RechercheForm()

            return form
        return None 