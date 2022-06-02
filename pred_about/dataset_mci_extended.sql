
-- 2012-04-25

SELECT TOP (100000)
DATEDIFF(day, CONVERT(DATE, '2012-04-25'), dataset.DateMandat) as 'DateMandatInstant'
,CASE
    WHEN MONTH(dataset.DateMandat) < 3 OR (MONTH(dataset.DateMandat) = 3 AND DAY(dataset.DateMandat) < 21) THEN 1
    WHEN (MONTH(dataset.DateMandat) = 3 AND MONTH(dataset.DateMandat) >= 21) OR MONTH(dataset.DateMandat) < 6 OR (MONTH(dataset.DateMandat) = 6 AND DAY(dataset.DateMandat) < 21) THEN 2
    WHEN (MONTH(dataset.DateMandat) = 6 AND MONTH(dataset.DateMandat) >= 21) OR MONTH(dataset.DateMandat) < 9 OR (MONTH(dataset.DateMandat) = 9 AND DAY(dataset.DateMandat) < 21) THEN 3
    WHEN (MONTH(dataset.DateMandat) = 9 AND MONTH(dataset.DateMandat) >= 21) OR MONTH(dataset.DateMandat) < 12 OR (MONTH(dataset.DateMandat) = 12 AND DAY(dataset.DateMandat) < 21) THEN 4
    ELSE 1
END as 'DateMandatSeason'
,DATEDIFF(year, CONVERT(DATE, '2012-04-26'), dataset.DateMandat) as 'DateMandatYear'
,MONTH(dataset.DateMandat) as 'DateMandatMonth'
,DATEPART(week, dataset.DateMandat) as 'DateMandatWeek'
,*
FROM (
    SELECT TOP(100000)
    mandats.[MandatId],
    CONCAT('https://monespace.net-acheteur.com/Spa/app/#/mandat/', mandats.[MandatId]) as 'UrlMandat',
    mandats.[DateMandat],
    CASE mandats.[StatutMandat]
        WHEN 1 THEN 'Traitement du lead'
        WHEN 5 THEN 'Lead perdu'
        WHEN 6 THEN 'Mission en cours'
        WHEN 7 THEN 'Preparation de l''acte'
        WHEN 8 THEN 'Entrée dans les lieux'
        WHEN 9 THEN 'Mandat perdu'
        WHEN 12 THEN 'Vente du service'
        ELSE 'Inconnu'
    END as 'StatutMandat',
    mandats.[DateCompromis],
    CASE
        WHEN c.[BudgetMaxEuro] >= 1000 THEN c.[BudgetMaxEuro]
        WHEN c.[BudgetMaxEuro] < 1000 THEN c.[BudgetMaxEuro] * 1000
        ELSE c.[BudgetMaxEuro]
    END as 'BudgetMaxEuro',
    CASE c.[TypeBienEnum]
        WHEN 1 THEN 'Maison'
        WHEN 2 THEN 'Appartement'
        WHEN 3 THEN 'Terrain'
        WHEN 4 THEN 'Autre'
        WHEN 5 THEN 'Studio'
        WHEN 6 THEN 'Local'
        WHEN 7 THEN 'Maison ou appartement'
        WHEN 8 THEN 'Immeuble'
        ELSE 'Inconnu'
    END as 'TypeBien',
    c.[TypeProjet] as 'TypeProjet',
    c.[SurfaceMin] as 'SurfaceMin',
    CASE c.[NombrePiecesEnum]
        WHEN 1 THEN '1'
        WHEN 2 THEN '2'
        WHEN 3 THEN '3'
        WHEN 4 THEN '4'
        WHEN 5 THEN '5'
        WHEN 6 THEN '6+'
        ELSE 'Inconnu'
    END as 'NombrePieces',
    CASE c.[NombreChambresEnum]
        WHEN 1 THEN '1'
        WHEN 2 THEN '2'
        WHEN 3 THEN '3'
        WHEN 4 THEN '4'
        WHEN 5 THEN '5'
        WHEN 6 THEN '6+'
        ELSE 'Inconnu'
    END as 'NombreChambres',
    localisation.Nom as 'Ville',
    localisation.Code as 'CodePostal',
    departement.Nom as 'Departement',
    region.Nom as 'Region',
    mandats.NombreDeBiensTrouves,
    mandats.NombreDeBiensPublies,
    mandats.NombreDeBiensSelectionnes,
    mandats.NombreDeBiensAVisiter,
    mandats.NombreDeBiensVisites,
    mandats.NombreDeBiensRejetes,
    mandats.NombreDeBiensActesOuCompromis,
    mandats.DatePremierePublicationDeBien,
    mandats.DateDernierePublicationDeBien,
    mandats.DelaiPremierePublicationDeBien,
    mandats.DatePremiereVisite,
    mandats.DelaiPremiereVisite
    FROM (
        SELECT TOP(100000)
        m.[MandatId],
        m.[CritereId],
        m.[StatutProspectMandatClientId] as 'StatutMandat',
        CASE 
            WHEN m.[DateMandatSignature] IS NOT NULL AND m.[DateMandatSignature] < m.[DateCreation] THEN CONVERT(DATE, m.[DateMandatSignature])
            ELSE CONVERT(DATE, m.[DateCreation])
        END as 'DateMandat',
        CONVERT(DATE, m.[DateCompromisSignature]) as 'DateCompromis',
        COUNT(bm.MandatId) as 'NombreDeBiensTrouves',
        SUM(CASE bm.[IsPublieClient]
            WHEN 1 THEN 1
            ELSE 0
        END) as 'NombreDeBiensPublies',
        SUM(CASE
            WHEN bm.[Statut] = 2 AND bm.[IsSupprime] = 0 THEN 1
            WHEN bm.[Statut] = 3 AND bm.[IsPublieClient] = 1 AND bm.[IsSupprime] = 0 THEN 1
            WHEN bm.[Statut] IN (4, 5, 6) AND bm.[IsPublieClient] = 1 AND bm.[IsSupprime] = 0 THEN 1
            WHEN bm.[Statut] = 7 AND bm.[IsPublieClient] = 1 AND bm.[IsSupprime] = 1 THEN 1
            ELSE 0
        END) as 'NombreDeBiensSelectionnes',
        SUM(CASE
            WHEN bm.[Statut] = 3 AND bm.[IsPublieClient] = 1 AND bm.[IsSupprime] = 0 THEN 1
            ELSE 0
        END) as 'NombreDeBiensAVisiter',
        SUM(CASE
            WHEN bm.[Statut] IN (4, 5, 6) AND bm.[IsPublieClient] = 1 AND bm.[IsSupprime] = 0 THEN 1
            WHEN bm.[Statut] = 7 AND bm.[IsPublieClient] = 1 AND bm.[IsSupprime] = 1 THEN 1
            ELSE 0
        END) as 'NombreDeBiensVisites',
        SUM(CASE
            WHEN bm.[Statut] = 7 AND bm.[IsPublieClient] = 1 AND bm.[IsSupprime] = 0 THEN 1
            ELSE 0
        END) as 'NombreDeBiensRejetes',
        SUM(CASE
            WHEN bm.[Statut] IN (5, 6) AND bm.[IsPublieClient] = 1 AND bm.[IsSupprime] = 0 THEN 1
            ELSE 0
        END) as 'NombreDeBiensActesOuCompromis',
        MIN(CONVERT(DATE, bm.[DatePublicationClient])) as 'DatePremierePublicationDeBien',
        MAX(CONVERT(DATE, bm.[DatePublicationClient])) as 'DateDernierePublicationDeBien',
        DATEDIFF(day, CONVERT(DATE, CASE 
            WHEN m.[DateMandatSignature] IS NOT NULL AND m.[DateMandatSignature] < m.[DateCreation] THEN CONVERT(DATE, m.[DateMandatSignature])
            ELSE CONVERT(DATE, m.[DateCreation])
        END), MIN(CONVERT(DATE, bm.[DatePublicationClient]))) as 'DelaiPremierePublicationDeBien',
        CONVERT(DATE, MIN(bm.[DateProchaineVisite])) as 'DatePremiereVisite',
        DATEDIFF(day, CONVERT(DATE, CASE 
            WHEN m.[DateMandatSignature] IS NOT NULL AND m.[DateMandatSignature] < m.[DateCreation] THEN CONVERT(DATE, m.[DateMandatSignature])
            ELSE CONVERT(DATE, m.[DateCreation])
        END), CONVERT(DATE, MIN(bm.[DateProchaineVisite]))) as 'DelaiPremiereVisite'
        FROM [Mandat] m
        LEFT JOIN [BienMandat] bm ON bm.[MandatId] = m.MandatId
        WHERE m.[StatutProspectMandatClientId] IN (5, 7, 8, 9)
        GROUP BY m.[MandatId], m.[CritereId], m.[StatutProspectMandatClientId], m.[DateMandatSignature], m.[DateCompromisSignature], m.[DateCreation]
        ORDER BY m.[MandatId] DESC
    ) as mandats
    INNER JOIN [Criteres] c ON mandats.[CritereId] = c.[CritereId]
    INNER JOIN [LocalisationCritere] lc ON c.[CritereId] = lc.[CritereId]
    INNER JOIN [Localisation] localisation ON lc.[LocalisationId] = localisation.[LocalisationId] AND localisation.[Departement_LocalisationId] IS NOT NULL AND localisation.[Region_LocalisationId] IS NULL
    LEFT JOIN [Localisation] departement ON departement.[LocalisationId] = localisation.[Departement_LocalisationId]
    LEFT JOIN [Localisation] region ON region.[LocalisationId] = departement.[Region_LocalisationId]
    WHERE c.[BudgetMaxEuro] > 10 AND ((c.[TypeBienEnum] <> 8 AND c.[SurfaceMin] < 10000) OR (c.[TypeBienEnum] = 8)) AND c.[BudgetMaxEuro] <> 0 AND c.[TypeBienEnum] <> 0 AND LEN(c.[TypeProjet]) <> 0 AND c.[NombrePiecesEnum] <> 0 AND c.[NombreChambresEnum] <> 0
    ) as dataset
ORDER BY DateMandatInstant;
