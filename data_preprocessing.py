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



def clean_value(x):
    if pd.notna(x):
        x = x.strip('[ "')
        x = x[0:4]
        return x
    else:
        return x


def prepare_data_40():
    adresse = pd.read_csv('adresse.csv', sep=';')
    rel_batiment_construction_adresse = pd.read_csv('rel_batiment_construction_adresse.csv', sep=';')
    batiment_construction = pd.read_csv('batiment_construction.csv', sep=";")
    batiment_groupe_rnc = pd.read_csv('batiment_groupe_rnc.csv', sep=';')
    batiment_groupe = pd.read_csv('batiment_groupe.csv', sep=';')
    batiment_groupe_argiles = pd.read_csv('batiment_groupe_argiles.csv', sep=';')
    batiment_groupe_bdtopo_bat = pd.read_csv('batiment_groupe_bdtopo_bat.csv', sep=';')
    adresse_metrique = pd.read_csv('adresse_metrique.csv', sep=';')
    rel_batiment_cons_adr_unique = rel_batiment_construction_adresse.drop_duplicates(subset=['cle_interop_adr'])
    rel_batiment_cons_adr_unique1 = rel_batiment_construction_adresse.drop_duplicates(
        subset=['batiment_construction_id'])
    merged_data = pd.merge(adresse, rel_batiment_cons_adr_unique, on='cle_interop_adr', how='inner')
    merged_data_1 = pd.merge(batiment_construction, rel_batiment_cons_adr_unique1, on='batiment_construction_id',
                             how='inner')
    combined_data_adresse_batiment_rel = pd.merge(merged_data_1, merged_data,
                                                  on=['batiment_construction_id', 'cle_interop_adr'], how='inner')
    merged_data3 = pd.merge(batiment_groupe_rnc, batiment_groupe, on='batiment_groupe_id', how='inner')

    # Appliquer la fonction à la colonne 'l_annee_construction'
    merged_data3['l_annee_construction'] = merged_data3['l_annee_construction'].apply(clean_value)
    merged_data3['l_annee_construction'].unique()
    merged_data_7 = pd.merge(combined_data_adresse_batiment_rel, batiment_groupe_argiles, on='batiment_groupe_id',
                             how='left')
    merged_data_8 = pd.merge(merged_data_7, merged_data3, on='batiment_groupe_id', how='left')
    #merged_data_9 = pd.merge(merged_data_8, batiment_groupe_bdtopo_bat, on='batiment_groupe_id', how='left')
    merged_data_9 = pd.merge(merged_data_8, batiment_groupe_bdtopo_bat, on='batiment_groupe_id', how='left',
                             suffixes=('_merged_data_8', '_batiment_groupe_bdtopo_bat'))
    merged_data_10 = pd.merge(merged_data_9, adresse_metrique, on='cle_interop_adr', how='left')
    colonnes_a_garder = ['WKT_x_y', 'libelle_adresse', 'altitude_sol', 's_geom_cstr', 'alea', 'l_nature', 'l_etat','hauteur',
                         'l_usage_1', 'l_usage_2', 'nb_bat_grp']
    merged_data_10 = merged_data_10.loc[:, colonnes_a_garder]
    merged_data_10.to_csv('combined_map_near_sea_40.csv', index=False)


def prepare_data_33_fort():
    adresse = pd.read_csv('adresse.csv', sep=';')
    rel_batiment_construction_adresse = pd.read_csv('rel_batiment_construction_adresse.csv', sep=';')
    batiment_construction = pd.read_csv('batiment_construction.csv', sep=";")
    batiment_groupe_rnc = pd.read_csv('batiment_groupe_rnc.csv', sep=';')
    batiment_groupe = pd.read_csv('batiment_groupe.csv', sep=';')
    batiment_groupe_argiles = pd.read_csv('batiment_groupe_argiles.csv', sep=';')
    batiment_groupe_bdtopo_bat = pd.read_csv('batiment_groupe_bdtopo_bat.csv', sep=';')
    adresse_metrique = pd.read_csv('adresse_metrique.csv', sep=';')
    rel_batiment_cons_adr_unique = rel_batiment_construction_adresse.drop_duplicates(subset=['cle_interop_adr'])
    rel_batiment_cons_adr_unique1 = rel_batiment_construction_adresse.drop_duplicates(
        subset=['batiment_construction_id'])
    merged_data = pd.merge(adresse, rel_batiment_cons_adr_unique, on='cle_interop_adr', how='inner')
    merged_data_1 = pd.merge(batiment_construction, rel_batiment_cons_adr_unique1, on='batiment_construction_id',
                             how='inner')
    combined_data_adresse_batiment_rel = pd.merge(merged_data_1, merged_data,
                                                  on=['batiment_construction_id', 'cle_interop_adr'], how='inner')
    merged_data3 = pd.merge(batiment_groupe_rnc, batiment_groupe, on='batiment_groupe_id', how='inner')

    # Appliquer la fonction à la colonne 'l_annee_construction'
    merged_data3['l_annee_construction'] = merged_data3['l_annee_construction'].apply(clean_value)
    merged_data3['l_annee_construction'].unique()
    merged_data_7 = pd.merge(combined_data_adresse_batiment_rel, batiment_groupe_argiles, on='batiment_groupe_id',
                             how='left')
    merged_data_8 = pd.merge(merged_data_7, merged_data3, on='batiment_groupe_id', how='left')
    #merged_data_9 = pd.merge(merged_data_8, batiment_groupe_bdtopo_bat, on='batiment_groupe_id', how='left')
    merged_data_9 = pd.merge(merged_data_8, batiment_groupe_bdtopo_bat, on='batiment_groupe_id', how='left',
                             suffixes=('_merged_data_8', '_batiment_groupe_bdtopo_bat'))
    merged_data_10 = pd.merge(merged_data_9, adresse_metrique, on='cle_interop_adr', how='left')
    colonnes_a_garder = ['WKT_x_y', 'libelle_adresse', 'altitude_sol', 's_geom_cstr', 'alea', 'l_nature', 'l_etat','hauteur',
                         'l_usage_1', 'l_usage_2', 'nb_bat_grp']
    merged_data_10 = merged_data_10.loc[:, colonnes_a_garder]
    merged_data_10.to_csv('combined_map_near_sea_33_fort.csv', index=False)


def prepare_data_33_autre():
    adresse = pd.read_csv('adresse.csv', sep=';')
    rel_batiment_construction_adresse = pd.read_csv('rel_batiment_construction_adresse.csv', sep=';')
    batiment_construction = pd.read_csv('batiment_construction.csv', sep=";")
    batiment_groupe_rnc = pd.read_csv('batiment_groupe_rnc.csv', sep=';')
    batiment_groupe = pd.read_csv('batiment_groupe.csv', sep=';')
    batiment_groupe_argiles = pd.read_csv('batiment_groupe_argiles.csv', sep=';')
    batiment_groupe_bdtopo_bat = pd.read_csv('batiment_groupe_bdtopo_bat.csv', sep=';')
    adresse_metrique = pd.read_csv('adresse_metrique.csv', sep=';')
    rel_batiment_cons_adr_unique = rel_batiment_construction_adresse.drop_duplicates(subset=['cle_interop_adr'])
    rel_batiment_cons_adr_unique1 = rel_batiment_construction_adresse.drop_duplicates(
        subset=['batiment_construction_id'])
    merged_data = pd.merge(adresse, rel_batiment_cons_adr_unique, on='cle_interop_adr', how='inner')
    merged_data_1 = pd.merge(batiment_construction, rel_batiment_cons_adr_unique1, on='batiment_construction_id',
                             how='inner')
    combined_data_adresse_batiment_rel = pd.merge(merged_data_1, merged_data,
                                                  on=['batiment_construction_id', 'cle_interop_adr'], how='inner')
    merged_data3 = pd.merge(batiment_groupe_rnc, batiment_groupe, on='batiment_groupe_id', how='inner')

    # Appliquer la fonction à la colonne 'l_annee_construction'
    merged_data3['l_annee_construction'] = merged_data3['l_annee_construction'].apply(clean_value)
    merged_data3['l_annee_construction'].unique()
    merged_data_7 = pd.merge(combined_data_adresse_batiment_rel, batiment_groupe_argiles, on='batiment_groupe_id',
                             how='left')
    merged_data_8 = pd.merge(merged_data_7, merged_data3, on='batiment_groupe_id', how='left')
    #merged_data_9 = pd.merge(merged_data_8, batiment_groupe_bdtopo_bat, on='batiment_groupe_id', how='left')
    merged_data_9 = pd.merge(merged_data_8, batiment_groupe_bdtopo_bat, on='batiment_groupe_id', how='left',
                             suffixes=('_merged_data_8', '_batiment_groupe_bdtopo_bat'))
    merged_data_10 = pd.merge(merged_data_9, adresse_metrique, on='cle_interop_adr', how='left')
    colonnes_a_garder = ['WKT_x_y', 'libelle_adresse', 'altitude_sol', 's_geom_cstr', 'alea', 'l_nature', 'l_etat','hauteur',
                         'l_usage_1', 'l_usage_2', 'nb_bat_grp']
    merged_data_10 = merged_data_10.loc[:, colonnes_a_garder]
    merged_data_10.to_csv('combined_map_near_sea_33_moyen_null.csv', index=False)


def prepare_data_17():
    adresse = pd.read_csv('adresse.csv', sep=';')
    rel_batiment_construction_adresse = pd.read_csv('rel_batiment_construction_adresse.csv', sep=';')
    batiment_construction = pd.read_csv('batiment_construction.csv', sep=";")
    batiment_groupe_rnc = pd.read_csv('batiment_groupe_rnc.csv', sep=';')
    batiment_groupe = pd.read_csv('batiment_groupe.csv', sep=';')
    batiment_groupe_argiles = pd.read_csv('batiment_groupe_argiles.csv', sep=';')
    batiment_groupe_bdtopo_bat = pd.read_csv('batiment_groupe_bdtopo_bat.csv', sep=';')
    adresse_metrique = pd.read_csv('adresse_metrique.csv', sep=';')
    rel_batiment_cons_adr_unique = rel_batiment_construction_adresse.drop_duplicates(subset=['cle_interop_adr'])
    rel_batiment_cons_adr_unique1 = rel_batiment_construction_adresse.drop_duplicates(
        subset=['batiment_construction_id'])
    merged_data = pd.merge(adresse, rel_batiment_cons_adr_unique, on='cle_interop_adr', how='inner')
    merged_data_1 = pd.merge(batiment_construction, rel_batiment_cons_adr_unique1, on='batiment_construction_id',
                             how='inner')
    combined_data_adresse_batiment_rel = pd.merge(merged_data_1, merged_data,
                                                  on=['batiment_construction_id', 'cle_interop_adr'], how='inner')
    merged_data3 = pd.merge(batiment_groupe_rnc, batiment_groupe, on='batiment_groupe_id', how='inner')

    # Appliquer la fonction à la colonne 'l_annee_construction'
    merged_data3['l_annee_construction'] = merged_data3['l_annee_construction'].apply(clean_value)
    merged_data3['l_annee_construction'].unique()
    merged_data_7 = pd.merge(combined_data_adresse_batiment_rel, batiment_groupe_argiles, on='batiment_groupe_id',
                             how='left')
    merged_data_8 = pd.merge(merged_data_7, merged_data3, on='batiment_groupe_id', how='left')
    #merged_data_9 = pd.merge(merged_data_8, batiment_groupe_bdtopo_bat, on='batiment_groupe_id', how='left')
    merged_data_9 = pd.merge(merged_data_8, batiment_groupe_bdtopo_bat, on='batiment_groupe_id', how='left',
                             suffixes=('_merged_data_8', '_batiment_groupe_bdtopo_bat'))
    merged_data_10 = pd.merge(merged_data_9, adresse_metrique, on='cle_interop_adr', how='left')
    colonnes_a_garder = ['WKT_x_y', 'libelle_adresse', 'altitude_sol', 's_geom_cstr', 'alea', 'l_nature', 'l_etat','hauteur',
                         'l_usage_1', 'l_usage_2', 'nb_bat_grp']
    merged_data_10 = merged_data_10.loc[:, colonnes_a_garder]
    merged_data_10.to_csv('combined_map_near_sea_17.csv', index=False)



if __name__ == '__main__':
      prepare_data_33_autre()
      #prepare_data_40()
