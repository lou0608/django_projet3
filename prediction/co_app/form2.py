from django import forms
from prediction.models import ChasseursInscription 


class ChasseursForm(forms.ModelForm):
    class Meta:
        model = ChasseursInscription
        fields = "__all__"