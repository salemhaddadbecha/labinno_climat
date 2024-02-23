# Importing necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical calculations
from shapely.geometry import Point  # For geometric operations
import pyproj  # For coordinate transformations
import folium  # For creating interactive maps
import geopandas as gpd  # For working with geospatial data
from folium.plugins import MarkerCluster  # For clustering markers on the map
from html5validator.validator import Validator
import tempfile
import subprocess
from IPython.display import IFrame

def validate_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Créer un fichier temporaire et écrire le contenu HTML
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_file.write(html_content)
        temp_file_path = temp_file.name

    validator = Validator()
    result = validator.validate([temp_file_path])  # Passer le chemin du fichier temporaire

    # Supprimer le fichier temporaire après validation
    subprocess.run(['rm', temp_file_path])

    if result.is_valid:
        print("Le fichier HTML est valide.")
    else:
        print("Le fichier HTML contient des erreurs de validation :")
        for error in result.messages:
            print(error)



if __name__ == '__main__':
      validate_html_file('templates/combined_map_near_sea_17.html')

