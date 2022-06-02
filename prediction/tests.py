from django.test import TestCase

# Create your tests here.
 
# definir les fonctions /fonctionalité les plus importantes a tester 
# test les methodes
# from truc machin # import pred
# test data dur fonction 
# analyse du fonctionnement
# on peut verifier le type de la variable
# verification de resultat

import unittest
from django.test import Client
import pandas as pd
import numpy as np
from prediction.utilities.format_data import build_plotly_df

class SimpleTest(unittest.TestCase):
    def test_exemple(self):
        self.assertEqual(True, True)
        
    def test_build_plotly_df(self):
        df_test = pd.DataFrame(np.eye(13, k=1))
        df_test = build_plotly_df(df_test)
        rename_column = ["MandatId", "StatutProspectMandatClientID", "SurfaceMin", "NombrePiecesEnum", "NombreChambresEnum", "TypeProjet", "TypeBien", "Region_LocalisationId", "BudgetMaxEuro", "CodePostal", "Departement", "Ville","Region"]        
        print(df_test.columns)
        self.assertEqual(df_test.columns.to_list(), rename_column)





