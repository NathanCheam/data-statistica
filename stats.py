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

def lecture_fichierCSV(fichier) :
    try :
        df = pd.read_csv(str(fichier)+".csv")
        print("Lecture du fichier | Effectuée")
        return df
    except FileNotFoundError :
        print("Le fichier saisi n'existe pas")
        return 0

def supprimer_fichierCSV(fichier) :
    try :
        os.remove(str(fichier)+".csv")
        print("Suppression du fichier | Effectuée")
    except FileNotFoundError :
        print("Le fichier "+str(fichier)+" n'existe pas")
        return 0
    except PermissionError :
        print("Vous n'avez pas la permission pour supprimer : "+str(fichier))
    except Exception as e :
        print("Une erreur s'est produite : "+str(e))

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

def moyenne(fichier) :
    df = lecture_fichierCSV(fichier)
    resultat = np.mean(df['Y'])
    return resultat

def mediane(fichier) :
    df = lecture_fichierCSV(fichier)
    resultat = np.median(df['Y'])
    return resultat

# La variance mesure l'écart moyen au carré entre chaque valeur d'un ensemble de données et la moyenne de cet ensemble
# Donne une mesure brute de la dispersion globale des données
# Plus la variance est élevée, plus les données sont dispersées autour de la moyenne
def variance(fichier) :
    df = lecture_fichierCSV(fichier)
    resultat = np.var(df['Y'])
    return resultat

# L'écart-type est la racine carrée de la variance. Contrairement à la variance, il est exprimé dans la même unité que les données d'origine
# Donne une mesure intuitive de la dispersion globale des données, car il est exprimé dans la même unité que les données
# Une petite valeur d'écart-type signifie que les données sont regroupées près de la moyenne, tandis qu'une grande valeur indique une plus grande dispersion
def ecart_type(fichier) :
    df = lecture_fichierCSV(fichier)
    resultat = math.sqrt(variance(fichier))
    return resultat

'''
Exemple pratique :

Si vous avez un ensemble de notes d'élèves [10,12,14,16,18] :

    - Moyenne = 14.
    - Variance = (1/5)*((10−14)^2+(12−14)^2+(14−14)^2+(16−14)^2+(18−14)^2)=8
    - Écart-type = racine carrée de la variance : √8 ≈ 2.838

Cela signifie que les notes sont, en moyenne, dispersées d'environ 2.83 points autour de la moyenne 14.
'''

#TEST des fonctions existantes
"""
print("Saisissez un nom à votre nouveau fichier CSV")
print("Si vous saisissez le nom d'un fichier existant, alors le contenu de ce fichier sera remplacé avec les nouvelles données")
fichier = input()
nouvelles_donnees(fichier)
generer_histogramme(fichier)
print("La moyenne des valeurs de Y : "+str(moyenne(fichier)))
print("La médiane des valeurs de Y : "+str(mediane(fichier)))
print("La variance des valeurs de Y : "+str(variance(fichier)))
print("L'écart-type des valeurs de Y : "+str(ecart_type(fichier)))
print("Cela signifie que les notes sont, en moyenne, dispersées d'environ "+str(ecart_type(fichier))+" points autour de la moyenne "+str(moyenne(fichier))+".")
"""

print("Saisissez le nom du fichier CSV à supprimer :")
fichier2 = input()
supprimer_fichierCSV(fichier2)