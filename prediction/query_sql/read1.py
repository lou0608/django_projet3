from http.client import HTTPResponse
from mailbox import NotEmptyError
from django.shortcuts import render
from rest_framework.response import Response
from django.db import connection

from prediction.forms import RechercheForm
import pandas as pd

from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px

from prediction.utilities.format_data import build_plotly_df

from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://lou6:Kaleo.31310@localhost:3306/aboutissement")
conn = engine.connect()

def query1(request):
    if request.method == 'POST':
        form = RechercheForm(request.POST)
        if form.is_valid():
            cp = form['CodePostal'].value()
            query = """SELECT mandat.MandatId, SurfaceMin, NombrePiecesEnum, NombreChambresEnum, mandat.TypeDeMission as TypeMission, criteres.TypeBienEnum as TypeBien,
            criteres.TypeProjet, departement.Region_LocalisationId, mandat.StatutProspectMandatClientID,
            case criteres.BudgetMaxEuro
	            WHEN criteres.BudgetMaxEuro >= 1000 THEN criteres.BudgetMaxEuro
                WHEN criteres.BudgetMaxEuro < 1000 THEN criteres.BudgetMaxEuro * 1000
                ELSE criteres.BudgetMaxEuro
            END AS "BudgetMaxEuro",
                localisation.Code as "CodePostal",
                departement.Nom as 'Departement',
                localisation.Nom as "Ville",
                region.Nom as "Region"
            from mandat
                INNER JOIN Criteres on Criteres.CritereId = mandat.CritereId
                left JOIN Localisation_Criteres ON Localisation_Criteres.CritereId = criteres.CritereId
                INNER JOIN localisation ON localisation.LocalisationId = Localisation_Criteres.LocalisationId 
                AND localisation.Departement_LocalisationId IS NOT NULL AND localisation.Region_LocalisationId IS NULL
                LEFT JOIN Localisation departement ON departement.LocalisationId = localisation.Departement_LocalisationId
                LEFT JOIN Localisation region ON region.LocalisationId = departement.Region_LocalisationId
                WHERE mandat.StatutProspectMandatClientID in (7,8)
                and localisation.Code LIKE ({0}) ;""".format(cp)
              
            df = pd.read_sql_query(query, conn)
            #df2 = pd.DataFrame(df, columns=["MandatId", "StatutProspectMandatClientID", "SurfaceMin", "NombrePiecesEnum", "NombreChambresEnum", "TypeProjet", "TypeBien", "Region_LocalisationId", "BudgetMaxEuro", "CodePostal", "Departement", "Ville","Region"])
            #df2.to_csv("test.csv")
            
            df2 = build_plotly_df(df)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=df2['TypeProjet'].unique(),
                y=df2.TypeProjet.value_counts(),
                orientation='v'))
            fig.update_yaxes(title='Count')
            fig.update_traces(marker_color='rgb(35, 38, 110)', marker_line_color='rgb(1,1,10)',
                  marker_line_width=2, opacity=0.8)
            fig.update_layout(
                autosize = True, 
                width = 600 , 
                height = 600 ,
                title= "Repartition des types de projet",
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            plot_div = plot(fig, output_type='div', include_plotlyjs= False)
            
            
            df2["TypeBien"] = df2["TypeBien"].replace({0: "Inconnu", 1:"Maison", 2: "Appartement", 3:"Terrain", 4:"Autre", 5:"Studio", 6:"Local", 7: "M ou A", 8:"Immeuble"})
            trace = go.Pie(labels = df2.TypeBien.value_counts().index, values = df2.TypeBien.value_counts(), 
               textfont=dict(size=15), opacity = 0.8, hole = .3,
               marker=dict(colors=['MidnightBlue', 'purple'], 
               line=dict(color='#000000', width=1.5)))
            layout= go.Layout(title={'text': "Pourcentage des ventes par type de bien"})
            fig2 = go.Figure(data = [trace], layout = layout)
            fig2.update_traces(textposition='inside')
            fig2.update_layout(height=600, width=600, uniformtext_minsize=12, uniformtext_mode='hide')
            plot_div2 = plot(fig2, output_type='div', include_plotlyjs= False)
            
            v = df2.loc[df2["CodePostal"]==cp]
            z = v["Ville"][:1]
            
            y = df2.shape[0]
            
            if df2.shape[0] >= 50:
                return plot_div, plot_div2, z[0], y
            return None, None, None, None


