import pandas as pd
import pycountry

def __set_iso_code(country_name):
    ' Internal Helper Function'
    try:
        return pycountry.countries.lookup(country_name).alpha_3
    except LookupError:
        return None  

def get_iso_code(df):
    'Function to insert the iso column of the isocode of the dataset names'
    df['iso'] = df['country'].apply(__set_iso_code)
    return None 
