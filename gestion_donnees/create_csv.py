import math
import os
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import pandas as pd


def saisir_donnees() :
    print("Saisir les valeurs pour l'axe des abscisses")
    line1 = input()
    print("Saisir les valeurs pour l'axe des ordonnées")
    line2 = input()
    try:
        axe_abscisses = list(map(float, line1.split()))
        axe_ordonnees = list(map(float, line2.split()))

        if(len(axe_abscisses) != len(axe_ordonnees)) :
            print("Il doit y avoir le même nombre de valeurs dans les deux axes")
            return None, None

        return axe_abscisses, axe_ordonnees
    except ValueError:
        print("Les nombres saisis doivent être uniquement des nombres décimaux.")
        return None, None

def generer_csv(axe_abscisses, axe_ordonnees, fichierCSV) :
    donnees = {
        "X" : axe_abscisses,
        "Y" : axe_ordonnees
    }

    df = pd.DataFrame(donnees)
    nom_fichier = f"{fichierCSV}.csv"
    df.to_csv(nom_fichier, index=False)
    print("Les données ont été enregistrées dans un fichier CSV")


def nouvelles_donnees(fichier) :
    X, Y = saisir_donnees()
    generer_csv(X, Y, fichier)