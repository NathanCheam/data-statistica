import math
import os
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import pandas as pd


def lecture_fichierCSV(fichier) :
    try :
        df = pd.read_csv(str(fichier)+".csv")
        print("Lecture du fichier | Effectuée")
        return df
    except FileNotFoundError :
        print("Le fichier saisi n'existe pas")
        return 0

def mediane(fichier) :
    df = lecture_fichierCSV(fichier)
    resultat = np.median(df['Y'])
    return resultat