import math
import os
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import pandas as pd

# La variance mesure l'écart moyen au carré entre chaque valeur d'un ensemble de données et la moyenne de cet ensemble
# Donne une mesure brute de la dispersion globale des données
# Plus la variance est élevée, plus les données sont dispersées autour de la moyenne

def lecture_fichierCSV(fichier) :
    try :
        df = pd.read_csv(str(fichier)+".csv")
        print("Lecture du fichier | Effectuée")
        return df
    except FileNotFoundError :
        print("Le fichier saisi n'existe pas")
        return 0

def variance(fichier) :
    df = lecture_fichierCSV(fichier)
    resultat = np.var(df['Y'])
    return resultat