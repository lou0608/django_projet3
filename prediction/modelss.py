# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Bienmandat(models.Model):
    bienmandatid = models.AutoField(db_column='BienMandatId', primary_key=True)  # Field name made lowercase.
    origine_urlorigineannonce = models.TextField(db_column='Origine_UrlOrigineAnnonce', blank=True, null=True)  # Field name made lowercase.
    descriptionbien_titre = models.TextField(db_column='DescriptionBien_Titre', blank=True, null=True)  # Field name made lowercase.
    descriptionbien_description = models.TextField(db_column='DescriptionBien_Description', blank=True, null=True)  # Field name made lowercase.
    descriptionbien_adresse_codepostal = models.TextField(db_column='DescriptionBien_Adresse_CodePostal', blank=True, null=True)  # Field name made lowercase.
    descriptionbien_adresse_ville = models.TextField(db_column='DescriptionBien_Adresse_Ville', blank=True, null=True)  # Field name made lowercase.
    descriptionbien_typebienenum = models.IntegerField(db_column='DescriptionBien_TypeBienEnum', blank=True, null=True)  # Field name made lowercase.
    descriptionbien_nombrepiecesenum = models.IntegerField(db_column='DescriptionBien_NombrePiecesEnum', blank=True, null=True)  # Field name made lowercase.
    descriptionbien_nombrechambresenum = models.IntegerField(db_column='DescriptionBien_NombreChambresEnum', blank=True, null=True)  # Field name made lowercase.
    descriptionbien_surface = models.IntegerField(db_column='DescriptionBien_surface')  # Field name made lowercase.
    descriptionbien_prix = models.IntegerField(db_column='DescriptionBien_Prix', blank=True, null=True)  # Field name made lowercase.
    statut = models.IntegerField(db_column='Statut', blank=True, null=True)  # Field name made lowercase.
    commentairetravaux = models.TextField(db_column='CommentaireTravaux', blank=True, null=True)  # Field name made lowercase.
    mandatid = models.ForeignKey('Mandat1', models.DO_NOTHING, db_column='MandatId')  # Field name made lowercase.
    descriptionbien_dateoffreacceptee = models.DateField(db_column='DescriptionBien_DateOffreAcceptee', blank=True, null=True)  # Field name made lowercase.
    origine_datecollecte = models.DateField(db_column='Origine_DateCollecte', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bienmandat'


class Criteres(models.Model):
    critereid = models.AutoField(db_column='CritereId', primary_key=True)  # Field name made lowercase.
    lieu = models.TextField(db_column='Lieu', blank=True, null=True)  # Field name made lowercase.
    typeprojet = models.CharField(db_column='TypeProjet', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typebienenum = models.IntegerField(db_column='TypeBienEnum', blank=True, null=True)  # Field name made lowercase.
    budgetmaxeuro = models.BigIntegerField(db_column='BudgetMaxEuro', blank=True, null=True)  # Field name made lowercase.
    surfacemin = models.IntegerField(db_column='SurfaceMin', blank=True, null=True)  # Field name made lowercase.
    nombrepiecesenum = models.IntegerField(db_column='NombrePiecesEnum', blank=True, null=True)  # Field name made lowercase.
    nombrechambresenum = models.IntegerField(db_column='NombreChambresEnum', blank=True, null=True)  # Field name made lowercase.
    descriptionlibrerecherche = models.TextField(db_column='DescriptionLibreRecherche', blank=True, null=True)  # Field name made lowercase.
    commentairetravauxacceptes = models.TextField(db_column='CommentaireTravauxAcceptes', blank=True, null=True)  # Field name made lowercase.
    ancienneufbien = models.IntegerField(db_column='AncienNeufBien', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'criteres'


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


class Localisation(models.Model):
    localisationid = models.AutoField(db_column='LocalisationId', primary_key=True)  # Field name made lowercase.
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    nom = models.TextField(db_column='Nom', blank=True, null=True)  # Field name made lowercase.
    codeinsee = models.TextField(db_column='CodeInsee', blank=True, null=True)  # Field name made lowercase.
    discriminator = models.TextField(db_column='Discriminator', blank=True, null=True)  # Field name made lowercase.
    region_localisationid = models.ForeignKey('self', models.DO_NOTHING, db_column='Region_LocalisationId', blank=True, null=True)  # Field name made lowercase.
    departement_localisationid = models.ForeignKey('self', models.DO_NOTHING, db_column='Departement_LocalisationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localisation'


class LocalisationCriteres(models.Model):
    critereid = models.ForeignKey(Criteres, models.DO_NOTHING, db_column='CritereId')  # Field name made lowercase.
    localisationid = models.IntegerField(db_column='LocalisationId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localisation_criteres'


class Mandat1(models.Model):
    mandatid = models.AutoField(db_column='MandatId', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientId')  # Field name made lowercase.
    critereid = models.ForeignKey(Criteres, models.DO_NOTHING, db_column='CritereId')  # Field name made lowercase.
    criteresmoteurid = models.IntegerField(db_column='CriteresMoteurId')  # Field name made lowercase.
    statutprospectmandatclientid = models.IntegerField(db_column='StatutProspectMandatClientId')  # Field name made lowercase.
    datemandatsignature = models.DateField(db_column='DateMandatSignature', blank=True, null=True)  # Field name made lowercase.
    datecompromissignature = models.DateField(db_column='DateCompromisSignature', blank=True, null=True)  # Field name made lowercase.
    datecreation = models.DateField(db_column='DateCreation', blank=True, null=True)  # Field name made lowercase.
    typedemission = models.IntegerField(db_column='TypeDeMission', blank=True, null=True)  # Field name made lowercase.
    typedemandat = models.IntegerField(db_column='TypeDeMandat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mandat_1'


class PredictionBienmandat(models.Model):
    id = models.IntegerField(primary_key=True)
    origine_annonce = models.CharField(db_column='Origine_Annonce', max_length=255)  # Field name made lowercase.
    descriptionbien_titre = models.TextField(db_column='DescriptionBien_Titre')  # Field name made lowercase.
    descriptionbien_description = models.TextField(db_column='DescriptionBien_Description')  # Field name made lowercase.
    descriptionbien_adressepostal = models.TextField(db_column='DescriptionBien_AdressePostal')  # Field name made lowercase.
    descriptionbien_adresse_ville = models.TextField(db_column='DescriptionBien_Adresse_Ville')  # Field name made lowercase.
    descriptionbien_typebienenum = models.IntegerField(db_column='DescriptionBien_TypeBienEnum')  # Field name made lowercase.
    descriptionbien_nombrepiecesenum = models.IntegerField(db_column='DescriptionBien_NombrePiecesEnum')  # Field name made lowercase.
    descriptionbien_nombrechambresenum = models.IntegerField(db_column='DescriptionBien_NombreChambresEnum')  # Field name made lowercase.
    descriptionbien_surface = models.IntegerField(db_column='DescriptionBien_surface')  # Field name made lowercase.
    descriptionbien_prix = models.IntegerField(db_column='DescriptionBien_Prix')  # Field name made lowercase.
    statut = models.IntegerField(db_column='Statut')  # Field name made lowercase.
    commentairetravaux = models.TextField(db_column='CommentaireTravaux')  # Field name made lowercase.
    mandatid = models.IntegerField(db_column='MandatId')  # Field name made lowercase.
    descriptionbien_dateoffreacceptee = models.DateField(db_column='DescriptionBien_DateOffreAcceptee')  # Field name made lowercase.
    origine_datecollecte = models.DateField(db_column='Origine_DateCollecte')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prediction_bienmandat'


class PredictionCriteres(models.Model):
    critereid = models.IntegerField(db_column='CritereId', primary_key=True)  # Field name made lowercase.
    typeprojet = models.TextField(db_column='TypeProjet')  # Field name made lowercase.
    typebienenum = models.IntegerField(db_column='TypeBienEnum')  # Field name made lowercase.
    budgetmaxeuro = models.IntegerField(db_column='BudgetMaxEuro')  # Field name made lowercase.
    nombrepiecesenum = models.IntegerField(db_column='NombrePiecesEnum')  # Field name made lowercase.
    nombrechambresenum = models.IntegerField(db_column='NombreChambresEnum')  # Field name made lowercase.
    descriptionlibrerecherche = models.TextField(db_column='DescriptionLibreRecherche')  # Field name made lowercase.
    commenatiretravauxacceptes = models.TextField(db_column='CommenatireTravauxAcceptes')  # Field name made lowercase.
    ancienbienneuf = models.IntegerField(db_column='AncienBienNeuf')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prediction_criteres'


class PredictionLocalisation(models.Model):
    localisationid = models.IntegerField(db_column='LocalisationId', primary_key=True)  # Field name made lowercase.
    code = models.TextField(db_column='Code')  # Field name made lowercase.
    nom = models.TextField(db_column='Nom')  # Field name made lowercase.
    codeinsee = models.TextField(db_column='CodeInsee')  # Field name made lowercase.
    discriminator = models.TextField(db_column='Discriminator')  # Field name made lowercase.
    region_localisationid = models.IntegerField(db_column='Region_LocalisationId')  # Field name made lowercase.
    departement_localisationid = models.IntegerField(db_column='Departement_LocalisationId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prediction_localisation'


class PredictionLocalisationCriteres(models.Model):
    id = models.BigAutoField(primary_key=True)
    critereid = models.IntegerField(db_column='CritereID')  # Field name made lowercase.
    localisationid = models.IntegerField(db_column='LocalisationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prediction_localisation_criteres'


class PredictionMandat(models.Model):
    mandatid = models.IntegerField(db_column='MandatId', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientId')  # Field name made lowercase.
    critereid = models.IntegerField(db_column='CritereId')  # Field name made lowercase.
    criteremoteurid = models.IntegerField(db_column='CritereMoteurId')  # Field name made lowercase.
    statutprospectmandatclientid = models.IntegerField(db_column='StatutProspectMandatClientId')  # Field name made lowercase.
    datemandatsignature = models.DateField(db_column='DateMandatSignature')  # Field name made lowercase.
    datecompromissignature = models.DateField(db_column='DateCompromisSignature')  # Field name made lowercase.
    datecreation = models.DateField(db_column='DateCreation')  # Field name made lowercase.
    typedemission = models.IntegerField(db_column='TypeDeMission')  # Field name made lowercase.
    typedemandat = models.IntegerField(db_column='TypeDeMandat')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prediction_mandat'


class StatutProspect(models.Model):
    statutmandatclientid = models.AutoField(db_column='StatutMandatClientId', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomafficherapport = models.CharField(db_column='NomAfficheRapport', max_length=50, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'statut_prospect'
