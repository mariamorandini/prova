import pandas as pd
import geopandas as gpd
path_to_shapefile = './data/ne_10m_admin_0_countries'

# Read the shapefile
world = gpd.read_file(path_to_shapefile)
list_countries = world['NAME']

rename_map = {
    'United States': 'United States of America',
    "Cote d'Ivoire": "Côte d'Ivoire", 
    "Democratic Republic of Congo": "Dem. Rep. Congo", 
    'Central African Republic':'Central African Rep.', 
    'South Sudan': 'S. Sudan', 
    'Bosnia and Herzegovina': 'Bosnia and Herz.',
    'Dominican Republic': 'Dominican Rep.',
}

def rename_countries(df, column='country'):
    'Helper function to match with the pyplot, renames some of the countries'
    df[column] = df[column].replace(rename_map)
    return None 

def drop_countries(df, column='country', list_countries=list_countries): 
    'Helper function to match with the pyplot, drop some of the countries that no more exist'
    x = df[df[column].isin(list_countries)]
    return x





