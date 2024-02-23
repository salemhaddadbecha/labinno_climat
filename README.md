# Description du projet

L'objectif principal de ce projet est de créer une application web qui utilise des données géographiques pour évaluer les risques d'inondation des bâtiments, en prenant en compte les facteurs climatiques. Les données sont extraites de fichiers CSV et traitées à l'aide de Python et de différentes bibliothèques telles que pandas, numpy, shapely, pyproj, folium et geopandas. L'application offre aux utilisateurs une interface interactive pour visualiser les coordonnées géographiques des différents départements sur une carte. Ces données sont essentielles pour une analyse approfondie des risques d'investissement liés aux conditions climatiques et aux zones sujettes aux inondations.

## Contenu du projet

#### Le projet se compose des éléments suivants :

Fichiers Python :
main.py : Contient le code Flask pour exécuter l'application localement.

data_processing.py : Contient les fonctions pour préparer et traiter les données.

generate_map(17, 33_fort, 33_moyen_null, 40, 64).py : Contient les fonctions pour générer la carte interactive.

html_validator.py : Contient les fonctions pour valider les fichiers HTML.

BDNP_Climatique_IMMO_NOTEBOOK.ipynb: Ce fichier contient des détails sur la partie extraction, préparation et modélisation des données.

Fichiers CSV :
adresse.csv, rel_batiment_construction_adresse.csv, batiment_construction.csv, etc. : Fichiers de données contenant des informations géographiques.

Fichiers HTML :
index.html : Page d'accueil avec un menu pour accéder aux différents départements.
combined_map_near_sea_17.html, combined_map_near_sea_33.html, etc. : Pages HTML pour afficher les cartes de chaque département.

Déploiement AWS :
Les fichiers HTML sont déployés sur AWS S3 pour permettre un accès public à l'application web statique.
Route 53 peut être utilisé pour la gestion du nom de domaine, mais des frais s'appliquent.
Fonctionnalités de l'application

### L'application permet aux utilisateurs de :

- Accéder à une page d'accueil avec un menu pour choisir un département.

- Visualiser les coordonnées géographiques des différents départements sur une carte interactive.

- Accéder à des pages HTML spécifiques pour chaque département pour une visualisation détaillée.

Pour exécuter l'application localement, exécutez le fichier main.py à l'aide de Flask. Les différentes routes permettent d'accéder aux différentes fonctionnalités de l'application.

- Déploiement sur AWS:

Les fichiers HTML sont déployés sur AWS S3 pour permettre un accès public à l'application. Un nom de domaine est configuré avec Route 53 pour une meilleure accessibilité.