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

def generer_histogramme(fichier) :
    df = lecture_fichierCSV(fichier)
    plt.figure(figsize=(8,6))
    plt.bar(df['X'], df['Y'], color='skyblue', edgecolor='black', width=0.8)
    plt.title('Histogramme des données du fichier CSV : '+str(fichier), fontsize=16)
    plt.xlabel('Valeurs de X', fontsize=14)
    plt.ylabel('Valeurs de Y', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(df['X'])
    plt.yticks(df['Y'])
    plt.show()