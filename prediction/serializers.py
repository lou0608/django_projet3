from rest_framework import serializers
from .models import Bienmandat, Criteres, Localisation,  Mandat, Form_Register, Localisation_Criteres
#, Chasseurs

# Serializers = permet de convertir les données en types python pour creer des json
# fonctionnent de manière similaire aux Forms
# permet de controler la sortie des reponses

class BienMandatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bienmandat
        fields = '__all__'

class CriteresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteres
        fields = '__all__'
        
class LocalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localisation
        fields = '__all__'

class Localisation_criteresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localisation_Criteres
        fields = '__all__'

class MandatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandat
        fields = '__all__'

        
class Form_RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form_Register
        fields = '__all__'


# class ChasseursSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Chasseurs
#         fields = '__all__'