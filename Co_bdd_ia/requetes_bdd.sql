-- Ma base de données :

select * from bienmandat ;
select * from criteres;
select * from localisation;
select * from localisation_criteres;
select * from mandat;
select * from statut_prospect


delete from django_migrations where id in (22,23)
-- Requetes : 

select mandat.MandatId, DateCreation, BienMandatId, Statut, DescriptionBien_DateOffreAcceptee,
Origine_DateCollecte, criteres.CritereId, TypeProjet, BudgetMaxEuro,
SurfaceMin, NombrePiecesEnum, NombreChambresEnum, 
localisation.Departement_LocalisationId, departement.Region_LocalisationId, Localisation_Criteres.LocalisationId,

case mandat.StatutProspectMandatClientID         
	WHEN 1 THEN 'Traitement du lead'
        WHEN 5 THEN 'Lead perdu'
        WHEN 6 THEN 'Mission en cours'
        WHEN 7 THEN "Preparation de l'acte"
        WHEN 8 THEN 'Entrée dans les lieux'
        WHEN 9 THEN 'Mandat perdu'
        WHEN 12 THEN 'Vente du service'
        ELSE 'Inconnu'
end as StatutMandat, 
case mandat.TypeDeMission
		WHEN 0 THEN 'Inconnu'
        WHEN 1 THEN 'Online'
        WHEN 2 THEN 'Terrain'
        WHEN 3 THEN 'Neuf'
        WHEN 4 THEN 'Vente'
        WHEN 5 THEN 'Location'
        WHEN 6 THEN "Apport d'affaires"
end as TypeMission,
case mandat.TypeDeMandat
	WHEN 0 THEN 'Exclusif'
        WHEN 1 THEN "Semi-exclusif"
        WHEN 2 THEN "Avec préavis"
end as TypeMandat,
case criteres.TypeBienEnum
	WHEN 1 THEN 'Maison'
        WHEN 2 THEN 'Appartement'
        WHEN 3 THEN 'Terrain'
        WHEN 4 THEN 'Autre'
        WHEN 5 THEN 'Studio'
        WHEN 6 THEN 'Local'
        WHEN 7 THEN 'Maison ou appartement'
        WHEN 8 THEN 'Immeuble'
        ELSE 'Inconnu'
END as TypeBien,
localisation.Code as "CodePostal",
localisation.Nom as "Ville",
departement.Nom as 'Departement',
region.Nom as 'Region'
from mandat
left JOIN BienMandat on BienMandat.MandatId = mandat.MandatId
INNER JOIN Criteres on Criteres.CritereId = mandat.CritereId
left JOIN Localisation_Criteres ON Localisation_Criteres.CritereId = criteres.CritereId

INNER JOIN localisation ON localisation.LocalisationId = Localisation_Criteres.LocalisationId 
AND localisation.Departement_LocalisationId IS NOT NULL AND localisation.Region_LocalisationId IS NULL
LEFT JOIN Localisation departement ON departement.LocalisationId = localisation.Departement_LocalisationId
LEFT JOIN Localisation region ON region.LocalisationId = departement.Region_LocalisationId

WHERE BienMandatId is not null and Statut is not null


-- LIMIT 10;

Where mandat.MandatId = 4;


WHERE localisation.Departement_LocalisationId IS NOT NULL
AND localisation.Region_LocalisationId is NULL;

Select * from Localisation
Where LocalisationId in (16);
-- 4890, 4891, 4899, 4962, 36021, 118, 26);

Select * from Localisation_Criteres
where CritereId = 198;

select MandatId, CritereId from mandat
Where CritereId = 198;

select * from Criteres
where CritereId = 198;


inner join localisation as Dep on Dep.LocalisationId = localisation.Departement_LocalisationId
inner join localisation as Reg on Reg.LocalisationId = Dep.Region_LocalisationId

AND localisation.Departement_LocalisationId IS NOT NULL AND localisation.Region_LocalisationId IS NULL

LEFT JOIN Localisation departement ON departement.LocalisationId = localisation.Departement_LocalisationId
and 
LEFT JOIN Localisation region ON region.LocalisationId = localisation.Region_LocalisationId

WHERE localisation.Departement_LocalisationId IS NOT NULL
AND localisation.Region_LocalisationId is NULL


-- left JOIN localisation_criteres on localisation_criteres.LocalisationId = localisation.LocalisationId

-- left join localisation on localisation.LocalisationId = localisation_criteres.LocalisationId
-- and localisation.Departement_LocalisationId is not null and localisation.Region_LocalisationId is not null
-- left JOIN localisation on localisation_criteres.LocalisationId = localisation.LocalisationId
-- and localisation.Departement_LocalisationId IS NOT NULL AND localisation.Region_LocalisationId IS NULL

LEFT JOIN localisation on localisation.LocalisationId = localisation_criteres.LocalisationId 
-- and localisation.Departement_LocalisationId IS NOT NULL AND localisation.Region_LocalisationId IS NULL

LEFT JOIN localisation departement ON departement.LocalisationId = localisation.Departement_LocalisationId
LEFT JOIN localisation region ON region.LocalisationId = departement.Region_LocalisationId 

-- WHERE localisation.Departement_LocalisationId is not null



-- Where localisation.Code is not null
-- WHERE localisation.Departement_LocalisationId is not null
-- and localisation.Region_LocalisationId is null










-- and localisation.departement_LocalisationId is not null and localisation.Region_LocalisationId is not null

-- où / quand les mandats ont une localisation non nulle


-- WHERE mandat.MandatId != null 


#where Localisation.Code is not null and Localisation.Nom is not null

#DESCRIBE LOCALISATION

#inner join localisation on localisation_criteres.LocalisationId = localisation.LocalisationId 
#and localisation.Departement_LocalisationId IS NOT NULL AND localisation.Region_LocalisationId IS NULL

#localisation.Code as "CodePostal", 
#localisation.Nom as "Ville", 
#departement.Nom as 'Departement', 
#region.Nom as 'Region'















select mandat.MandatId, DateCreation, BienMandatId, Statut, DescriptionBien_DateOffreAcceptee,
 Origine_DateCollecte, criteres.CritereId, TypeProjet, BudgetMaxEuro,
 SurfaceMin, NombrePiecesEnum, NombreChambresEnum, localisation.LocalisationId, localisation.Code, localisation.Nom,
 #localisation.Region_LocalisationId, localisation.Departement_LocalisationId,  
case mandat.StatutProspectMandatClientID            
WHEN 1 THEN 'Traitement du lead'         
WHEN 5 THEN 'Lead perdu'         
WHEN 6 THEN 'Mission en cours'         
WHEN 7 THEN "Preparation de l'acte"         
WHEN 8 THEN 'Entrée dans les lieux'         
WHEN 9 THEN 'Mandat perdu'         
WHEN 12 THEN 'Vente du service'         
ELSE 'Inconnu' end as StatutMandat,  
case mandat.TypeDeMission   
WHEN 0 THEN 'Inconnu'         
WHEN 1 THEN 'Online'         
WHEN 2 THEN 'Terrain'         
WHEN 3 THEN 'Neuf'         
WHEN 4 THEN 'Vente'         
WHEN 5 THEN 'Location'         
WHEN 6 THEN "Apport d'affaires" 
end as TypeMission, 
case mandat.TypeDeMandat   
WHEN 0 THEN 'Exclusif'         
WHEN 1 THEN "Semi-exclusif"         
WHEN 2 THEN "Avec préavis" 
end as TypeMandat, 
case criteres.TypeBienEnum   
WHEN 1 THEN 'Maison'         
WHEN 2 THEN 'Appartement'        
 WHEN 3 THEN 'Terrain'         
WHEN 4 THEN 'Autre'         
WHEN 5 THEN 'Studio'         
WHEN 6 THEN 'Local'         
WHEN 7 THEN 'Maison ou appartement'         
WHEN 8 THEN 'Immeuble'         
ELSE 'Inconnu' 
END as TypeBien 
from mandat 
inner join BienMandat on BienMandat.MandatId = mandat.MandatId 
inner join Criteres on Criteres.CritereId = mandat.CritereId 
inner join localisation_criteres on localisation_criteres.CritereId = criteres.CritereId 

left join localisation on localisation.LocalisationId = localisation_criteres.LocalisationId and localisation.Departement_LocalisationId IS NOT NULL AND localisation.Region_LocalisationId IS NULL 
LEFT JOIN Localisation departement ON departement.LocalisationId = localisation.Departement_LocalisationId 
LEFT JOIN Localisation region ON region.LocalisationId = departement.Region_LocalisationId  




 #DESCRIBE LOCALISATION    #Select * from localisation #Select * from localisation_criteres #select * from criteres    #inner join localisation on localisation_criteres.LocalisationId = localisation.LocalisationId  #and localisation.Departement_LocalisationId IS NOT NULL AND localisation.Region_LocalisationId IS NULL  #localisation.Code as "CodePostal",  #localisation.Nom as "Ville",  #departement.Nom as 'Departement',  #region.Nom as 'Region' LIMIT 0, 50000



DescriptionBien_TypeBienEnumDescriptionBien_NombreChambresEnumDescriptionBien_NombrePiecesEnum
DescriptionBien_surface
DescriptionBien_Prix
Statut
CommentaireTravaux
MandatId
DescriptionBien_DateOffreAcceptee
Origine_DateCollecte

CritereId
Lieen
u
TypeProjet
TypeBienEnum
BudgetMaxEuro
SurfaceMin
NombrePiecesEnum
NombreChambresEnum
DescriptionLibreRecherche
CommentaireTravauxAcceptesauth_user
AncienNeufBi

SELECT DISTINCT mandat.MandatId, mandat.DateCompromisSignature, bienmandat.DescriptionBien_DateOffreAcceptee, bienmandat.Statut, SurfaceMin, NombrePiecesEnum, NombreChambresEnum, mandat.TypeDeMission as TypeMission, criteres.TypeBienEnum as TypeBien,
case criteres.BudgetMaxEuro
	    WHEN criteres.BudgetMaxEuro >= 1000 THEN criteres.BudgetMaxEuro
        WHEN criteres.BudgetMaxEuro < 1000 THEN criteres.BudgetMaxEuro * 1000
        ELSE criteres.BudgetMaxEuro
END AS "BudgetMaxEuro",
case criteres.TypeProjet
	When criteres.TypeProjet = 'Investissement' THEN 0
    WHEN criteres.TypeProjet =  'Résidence principale' THEN 1
    WHEN criteres.TypeProjet = 'Résidence secondaire' THEN 2
    ELSE criteres.TypeProjet
END AS "TypeProjet",
localisation.Code as "CodePostal"
from mandat
left JOIN BienMandat on BienMandat.MandatId = mandat.MandatId
INNER JOIN Criteres on Criteres.CritereId = mandat.CritereId
left JOIN Localisation_Criteres ON Localisation_Criteres.CritereId = criteres.CritereId

INNER JOIN localisation ON localisation.LocalisationId = Localisation_Criteres.LocalisationId 
AND localisation.Departement_LocalisationId IS NOT NULL AND localisation.Region_LocalisationId IS NULL
LEFT JOIN Localisation departement ON departement.LocalisationId = localisation.Departement_LocalisationId
LEFT JOIN Localisation region ON region.LocalisationId = departement.Region_LocalisationId

WHERE bienmandat.Statut in (7,8)






















