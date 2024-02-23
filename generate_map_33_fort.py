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


def read_dataset():
    bdnp_33 = pd.read_csv('bdnp_33_map.csv')
    # Créer un DataFrame contenant uniquement les valeurs "Moyen" et les valeurs nulles
    bdnp_33_moyen_null = bdnp_33.loc[(bdnp_33['alea'] == 'Moyen') | bdnp_33['alea'].isnull()]

    # Créer un DataFrame contenant uniquement les valeurs "Fort"
    bdnp_33_fort = bdnp_33.loc[bdnp_33['alea'] == 'Fort']

    bdnp_33_fort.to_csv('combined_map_near_sea_33_fort.csv', index=False)

    bdnp_33_moyen_null.to_csv('combined_map_near_sea_33_moyen_null.csv', index=False)


def generating_map():
    bdnp_near_sea = pd.read_csv('combined_map_near_sea_33_fort.csv')

    # Defining Lambert-93 and WGS84 coordinate systems
    lambert_93 = pyproj.Proj(init='epsg:2154')  # Lambert-93 coordinate reference system
    wgs84 = pyproj.Proj(init='epsg:4326')  # WGS84 coordinate reference system (standard latitude and longitude)

    # Reading CSV file containing address data into a pandas DataFrame
    data = bdnp_near_sea  # 538455 rows in  28 min 29 secondes
    # 2743305 about 2 hours and 25 minutes.
    # Conversion of Lambert-93 coordinates to WGS84 using vectorized operations
    data['x_coords'] = data['WKT_x_y'].str.split().str[1].str[1:].astype(float)
    data['y_coords'] = data['WKT_x_y'].str.split().str[2].str[:-1].astype(float)
    lon, lat = pyproj.transform(lambert_93, wgs84, data['x_coords'], data['y_coords'])
    data['geometry'] = [Point(lon[i], lat[i]) for i in range(len(lon))]

    # Creating a GeoDataFrame from the DataFrame with a geometry column containing Point objects
    gdf = gpd.GeoDataFrame(data, geometry='geometry')

    # Creating a Folium map centered on the average latitude and longitude of the points with a zoom level of 7
    mymap = folium.Map(location=[gdf['geometry'].y.mean(), gdf['geometry'].x.mean()], zoom_start=1)

    # Creating a MarkerCluster object to group markers on the map
    marker_cluster = MarkerCluster().add_to(mymap)

    # Constructing the popup text for each row in the GeoDataFrame
    gdf['popup_text'] = (
            "Latitude: " + gdf['geometry'].y.astype(str) + ", <br>" +
            "Longitude: " + gdf['geometry'].x.astype(str) + ", <br>" +
            # peut etre prendre l'adresse directe et non pas en faisant l'` qui prend beaucoup de temps pour la combinaison.
            "Adresse: " + gdf['libelle_adresse'].astype(str) + ", <br>" +
            "Altitude_sol: " + gdf['altitude_sol'].astype(str) + ", <br>" +
            "Hauteur: " + gdf['hauteur'].astype(str) + ", <br>" +
            "Surface au sol[m²]: " + gdf['s_geom_cstr'].astype(str) + ", <br>" +
            "Aléa du risque argiles: " + gdf['alea'].astype(str) + ",<br>" +
            "Catégorie & Nature du bâtiment: " + gdf['l_nature'].astype(str) + ", <br>" +
            "Etat des bâtiments: " + gdf['l_etat'].astype(str) + ",  <br>" +
            "Usage principal du bâtiment: " + gdf['l_usage_1'].astype(str) + ", <br>"
        # "Usage secondaire du bâtiment: " + gdf['l_usage_2'].astype(str) + ", <br>" +
        # "Nombre de bâtiments desservis par l'adresse: " + gdf['nb_bat_grp'].astype(str)
    )

    # Create markers with popup text using vectorized approach
    for idx, row in gdf.iterrows():
        folium.Marker(location=[row['geometry'].y, row['geometry'].x], popup=row['popup_text']).add_to(marker_cluster)

    # Saving the map to an HTML file
    mymap.save('templates/combined_map_near_sea_33_fort.html')


def show_map(src):
    IFrame(src, width=800, height=350)


if __name__ == '__main__':
    generating_map()
# read_dataset()
