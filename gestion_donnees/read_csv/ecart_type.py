import math
import os
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import pandas as pd

# L'écart-type est la racine carrée de la variance. Contrairement à la variance, il est exprimé dans la même unité que les données d'origine
# Donne une mesure intuitive de la dispersion globale des données, car il est exprimé dans la même unité que les données
# Une petite valeur d'écart-type signifie que les données sont regroupées près de la moyenne, tandis qu'une grande valeur indique une plus grande dispersion

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

def ecart_type(fichier) :
    df = lecture_fichierCSV(fichier)
    resultat = math.sqrt(variance(fichier))
    return resultat