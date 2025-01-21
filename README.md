# Logiciel de gestion de données statistiques | par *CHEAM Nathan* (**En cours de réalisation**)

**Data-Statistica** est un logiciel conçu pour la gestion de données statistiques. Développé avec le framework PHP *Laravel*, il permet l'exécution de fonctions en *Python* et l'affichage de leurs retours. Ce logiciel s'appuie sur une base de données pour offrir des fonctionnalités complètes en matière de visualisation et de manipulation des statistiques.

---

## ⚙️ Fonctionnalités

- **Gestion des utilisateurs :** Création, modification et suppression des comptes utilisateurs
- **Gestion des données statistiques :** Ajout, modification, suppression et organisation des données.
- **Visualisation graphique :** Génération de graphiques interactifs et dynamiques.
- **Exécution de fonctions Python :** Lancement de scripts Python et affichage des résultats dans l'interface.
- **Exportation des données :** Possibilité d'exporter les données au format CSV ou Excel pour une analyse externe.

---

## 🛠️ Installation et exécution

### Prérequis

Avant de commencer, assurez-vous que les outils suivants sont installés sur votre système :
- **PHP** | *ddédé* (A partir de la version 8.0)
- **SQLite** | *Système de gestion de base de données*
- **Composer** | *Gestionnaire de dépendances PHP* (A partir de la version 2.0)
- **Laravel** | *Framework PHP*
- **Python** | *Langage de programmation* (A partir de la version 3.0)

### Étapes d'installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/NathanCheam/logiciel_stats.git
   cd logiciel_stats
   ```
2. Installez les dépendances :
   ```bash
    composer install
    ```
3. Configurez l'application :
    - Créez un fichier `.env` à partir du modèle `.env.example`
      ```bash
      cp .env.example .env
      ```
    - Modifiez le fichier .env pour configurer votre base de données (MySQL, SQLite, etc.)
    - Générez une clé d'application :
      ```bash
      php artisan key:generate
      ```
    - Rendre les fichiers stockés dans le dossier `storage/app/public` accessibles publiquement via le répertoire web `public/storage`
      ```bash
      php artisan storage:link
      ```
4. Mettez en place la base de données :
    ```bash
    php artisan migrate
    ```
5. Remplir la base de données avec des données initiales ou de test
   ```bash
   php artisan db:seed
   ```
6. Lancez le serveur de développement (accessible à l'adresse http://localhost:8000)
   ```bash
   php artisan serve
   ```