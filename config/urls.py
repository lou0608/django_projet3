"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from prediction.views import BienMandatViewSet, CriteresViewSet, LocalisationViewSet, Form_RegisterViewSet, Localisation_criteresViewSet
from prediction.views import MandatViewSet
#ChasseursViewSet

# un router permet de definir automatiquement toutes les URL accessibles pour un endpoint donné
router = DefaultRouter()
router.register(r'BienMandat', BienMandatViewSet, basename="BienMandat")
router.register(r'Criteres', CriteresViewSet, basename="Criteres")
router.register(r'Localisation', LocalisationViewSet, basename="Localisation")
router.register(r'Localisation_criteres', Localisation_criteresViewSet, basename="Localisation criteres")
router.register(r'Mandat', MandatViewSet, basename= "Mandat")
router.register(r'Form_Register', Form_RegisterViewSet, basename= "Prédiction")

#router.register(r'Chasseurs', ChasseursViewSet)

from prediction.views import Recherche, Signup, Auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("signup/", Signup, name = "registre-signup"),
    path('auth/', Auth,  name = "authentification-home-page"),
    path('home/', Recherche, name = "prediction-home-page"),
    ]

#import django.contrib.auth.urls