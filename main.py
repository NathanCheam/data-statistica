from gestion_donnees.read_csv.variance import variance
from gestion_donnees.read_csv.ecart_type import ecart_type
from gestion_donnees.read_csv.mediane import mediane
from gestion_donnees.read_csv.histogramme import generer_histogramme
from gestion_donnees.read_csv.moyenne import moyenne
from gestion_donnees.create_csv import nouvelles_donnees
from gestion_donnees.erase_csv import supprimer_fichierCSV

print("Bienvenue dans le programme de gestion de données")
print("1. Saisir de nouvelles données")
print("2. Supprimer un fichier CSV")
print("3. Quitter")
print()
print("Prenez votre décision")
choix = input()

match choix:
    case "1":
        print("Saisissez un nom à votre nouveau fichier CSV")
        print("Si vous saisissez le nom d'un fichier existant, alors le contenu de ce fichier sera remplacé avec les nouvelles données")
        fichier = input()
        nouvelles_donnees(fichier)
        generer_histogramme(fichier)
        print("La moyenne des valeurs de Y : " + str(moyenne(fichier)))
        print("La médiane des valeurs de Y : " + str(mediane(fichier)))
        print("La variance des valeurs de Y : " + str(variance(fichier)))
        print("L'écart-type des valeurs de Y : " + str(ecart_type(fichier)))
        print("Cela signifie que les notes sont, en moyenne, dispersées d'environ " + str(ecart_type(fichier)) + " points autour de la moyenne " + str(moyenne(fichier)) + ".")
    case "2":
        print("Saisissez le nom du fichier CSV à supprimer :")
        fichier2 = input()
        supprimer_fichierCSV(fichier2)
    case _:
        print("Choix invalide. Veuillez sélectionner 1 ou 2.")