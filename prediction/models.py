#from django.contrib.auth import get_user_model
#from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Declaration des données qui vont être utilisées
# Chaque classe correspond a une table de base de données

# blank = False :  champs ne peut pas être vide
# Create your models here.


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Localisation(models.Model):
    localisationid = models.IntegerField(db_column='LocalisationId', primary_key=True)
    # criteres = models.ManyToManyField(Criteres, through="Localisation_Criteres")
    # Field name made lowercase.
    code = models.TextField(db_column='Code')  # Field name made lowercase.
    nom = models.TextField(db_column='Nom')  # Field name made lowercase.
    codeinsee = models.TextField(db_column='CodeInsee')  # Field name made lowercase.
    discriminator = models.TextField(db_column='Discriminator')  # Field name made lowercase.
    region_localisationid = models.IntegerField(db_column='Region_LocalisationId')  # Field name made lowercase.
    departement_localisationid = models.IntegerField(db_column='Departement_LocalisationId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localisation'
        
        def __str__(self):
            return self.name
       
class Criteres(models.Model):
    critereid = models.IntegerField(db_column='CritereId', primary_key=True)  # Field name made lowercase.
    localisations = models.ManyToManyField(Localisation, through="Localisation_Criteres")
    typeprojet = models.TextField(db_column='TypeProjet')  # Field name made lowercase.
    typebienenum = models.IntegerField(db_column='TypeBienEnum')  # Field name made lowercase.
    budgetmaxeuro = models.IntegerField(db_column='BudgetMaxEuro')  # Field name made lowercase.
    nombrepiecesenum = models.IntegerField(db_column='NombrePiecesEnum')  # Field name made lowercase.
    nombrechambresenum = models.IntegerField(db_column='NombreChambresEnum')  # Field name made lowercase.
    descriptionlibrerecherche = models.TextField(db_column='DescriptionLibreRecherche')  # Field name made lowercase.
    commentairetravauxacceptes = models.TextField(db_column='CommentaireTravauxAcceptes')  # Field name made lowercase.
    ancienneufbien = models.IntegerField(db_column='AncienNeufBien')  # Field name made lowercase.

    class Meta:
        # managed = false ==> no create, delete, modify
        managed = False
        db_table = 'criteres'
        
        def __str__(self):
            return self.name  



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'    

class Localisation_Criteres(models.Model):
    #id = models.IntegerField(primary_key=True)
    critereid = models.ForeignKey(Criteres, db_column="CritereId", on_delete= models.CASCADE)# Field name made lowercase.
    localisationid = models.ForeignKey(Localisation, db_column="LocalisationId", on_delete= models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "localisation_criteres"
        
        def __str__(self):
            return self.name


class Mandat(models.Model):
    mandatid = models.IntegerField(db_column='MandatId', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientId')  # Field name made lowercase.
    critereid = models.ForeignKey(Criteres, db_column='CritereId', on_delete= models.CASCADE)  # Field name made lowercase.
    criteresmoteurid = models.IntegerField(db_column='CriteresMoteurId')  # Field name made lowercase.
    statutprospectmandatclientid = models.IntegerField(db_column='StatutProspectMandatClientId')  # Field name made lowercase.
    datemandatsignature = models.DateField(db_column='DateMandatSignature')  # Field name made lowercase.
    datecompromissignature = models.DateField(db_column='DateCompromisSignature')  # Field name made lowercase.
    datecreation = models.DateField(db_column='DateCreation')  # Field name made lowercase.
    typedemission = models.IntegerField(db_column='TypeDeMission')  # Field name made lowercase.
    typedemandat = models.IntegerField(db_column='TypeDeMandat')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mandat'
        
        def __str__(self):
            return self.name

class Bienmandat(models.Model):
    bienmandatid = models.IntegerField(db_column='BienMandatId',primary_key=True)
    origine_urlorigineannonce = models.CharField(db_column='Origine_UrlOrigineAnnonce', max_length=255)  # Field name made lowercase.
    descriptionbien_titre = models.TextField(db_column='DescriptionBien_Titre')  # Field name made lowercase.
    descriptionbien_description = models.TextField(db_column='DescriptionBien_Description')  # Field name made lowercase.
    descriptionbien_adresse_codepostal = models.TextField(db_column='DescriptionBien_Adresse_CodePostal')  # Field name made lowercase.
    descriptionbien_adresse_ville = models.TextField(db_column='DescriptionBien_Adresse_Ville')  # Field name made lowercase.
    descriptionbien_typebienenum = models.IntegerField(db_column='DescriptionBien_TypeBienEnum')  # Field name made lowercase.
    descriptionbien_nombrepiecesenum = models.IntegerField(db_column='DescriptionBien_NombrePiecesEnum')  # Field name made lowercase.
    descriptionbien_nombrechambresenum = models.IntegerField(db_column='DescriptionBien_NombreChambresEnum')  # Field name made lowercase.
    descriptionbien_surface = models.IntegerField(db_column='DescriptionBien_surface')  # Field name made lowercase.
    descriptionbien_prix = models.IntegerField(db_column='DescriptionBien_Prix')  # Field name made lowercase.
    statut = models.IntegerField(db_column='Statut')  # Field name made lowercase.
    commentairetravaux = models.TextField(db_column='CommentaireTravaux')  # Field name made lowercase.
    mandatid = models.ForeignKey(Mandat, on_delete=models.CASCADE, db_column='MandatId')  # Field name made lowercase.
    descriptionbien_dateoffreacceptee = models.DateField(db_column='DescriptionBien_DateOffreAcceptee')  # Field name made lowercase.
    origine_datecollecte = models.DateField(db_column='Origine_DateCollecte')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bienmandat'
        
        def __str__(self):
            return self.name
        

class Form_Register(models.Model):
    TypeMission = models.IntegerField(db_column ="Type de Mission")
    TypeBien = models.IntegerField(db_column = "Type de Bien")
    TypeProjet = models.IntegerField(db_column = "Type de Projet")
    CodePostal= models.IntegerField(db_column = "Code Postal")
    Budget = models.IntegerField(db_column = "Budget")
    NombrePieces = models.IntegerField(db_column = "Nombre de Pièces" )
    NombreChambres = models.IntegerField(db_column = "Nombre de Chambres")
    Surface = models.IntegerField(db_column = "Surface")
    Prediction = models.IntegerField(db_column="Prediction", default = 0, null = True, blank = True)
    
    class Meta:
        managed = True
        db_table = 'Form_Register'
        
        def __str__(self):
            return self.name

class ChasseursInscription(models.Model):
    Nom = models.CharField(db_column="Nom", max_length=25)
    Prenom = models.CharField(db_column="Prenom", max_length=25)
    Mot_de_passe = models.CharField(db_column="Mot_de_passe", max_length=8)
    Mot_de_passe2 = models.CharField(db_column="Mot_de_passe2", max_length=8, default = 0)
    Email = models.EmailField(db_column="Email")
    
    class Meta:
        managed = True
        db_table = 'ChasseursInscription'
        
        def __str__(self):
            return self.name
        
        
#Chasseurs = get_user_model()      
        
# class Chasseurs(models.Model):
#     #user_id = models.OneToOneField(User, on_delete=models.CASCADE, db_column="user_id")
#     username = models.CharField(db_column="username", max_length=250)
#     #password1 = models.CharField(db_column="password1", max_length=12)
#     Client_nom = models.CharField(db_column='Client_nom', blank = True, max_length=150)
#     Client_prenom = models.CharField(db_column='Client_prenom', blank = True, max_length=150)
#     Recherche = models.CharField(db_column='Recherche', blank = True,max_length=150)
#     USERNAME_FIELD = "UserID"
#     REQUIRED_FIELD = ["Prenom", "Nom"]
    
#     # def has_perm(self, perm, obj = None):
#     #     return True
    
#     # def has_module_perms(self, app_label):
#     #     return True
    
    # class Meta:
    #     managed = True
    #     db_table = 'Chasseurs'
        
    #     def __str__(self):
    #         return self.name   
    