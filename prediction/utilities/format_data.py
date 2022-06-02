import pandas as pd

def build_plotly_df(df):
    df2 = pd.DataFrame(df, columns=["MandatId", "StatutProspectMandatClientID", "SurfaceMin", "NombrePiecesEnum", "NombreChambresEnum", "TypeProjet", "TypeBien", "Region_LocalisationId", "BudgetMaxEuro", "CodePostal", "Departement", "Ville","Region"])
    df2["TypeProjet"] = df2["TypeProjet"].replace({0:"Investissement", 1:"Residence Principale", 2:"Residence Secondaire"})
    return df2

