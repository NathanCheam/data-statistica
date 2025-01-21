import math
import os
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import pandas as pd


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