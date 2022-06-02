from django import forms

# Déclaration du Formulaire

TYPEMISSION = ((0,"Inconnu"), (1,"Online"), (2,"Terrain"), (3,"Neuf"), (4,"Vente"), (5,"Location"), (6,"Apport d'affaires"))
TYPEBIEN = ((0,"Inconnu"),(1,"Maison"), (2,"Appartement"), (3,"Terrain"), (4,"Autre"), (5,"Studio"), (6,"Local"), (7,"Maison ou appartement"), (8,"Immeuble"))          
TYPEPROJET = ((0,"Investissement"), (1,"Résidence principale") , (2,"Résidence secondaire"))

NOMBREPIECES = ((1,1), (2,2), (3,3), (4,4), (5,5), (6,6))
NOMBRECHAMBRES = ((1,1), (2,2), (3,3), (4,4), (5,5), (6,6))

class RechercheForm(forms.Form):
    TypeMission = forms.ChoiceField(choices=TYPEMISSION, label = "Type de Mission")
    TypeBien = forms.ChoiceField(choices = TYPEBIEN, label = "Type de Bien")
    TypeProjet = forms.ChoiceField(choices = TYPEPROJET, label= "Type de Projet")
    CodePostal= forms.IntegerField(label = "Code Postal")
    Budget = forms.IntegerField(label = "Budget", min_value=5000)
    NombrePieces = forms.ChoiceField(choices = NOMBREPIECES, label = "Nombre de Pièces" )
    NombreChambres = forms.ChoiceField(choices = NOMBRECHAMBRES, label = "Nombre de Chambres")
    Surface = forms.IntegerField(label = "Surface")

    

    
    
    
