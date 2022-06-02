from django.contrib import admin

# Register your models here.

from prediction import models

admin.site.register(models.Bienmandat)
admin.site.register(models.Criteres)
admin.site.register(models.Localisation)
admin.site.register(models.Localisation_Criteres)
admin.site.register(models.Mandat)
admin.site.register(models.Form_Register)
#admin.site.register(models.Chasseurs)

