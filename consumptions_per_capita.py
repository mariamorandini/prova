import pandas as pd
def retain_consumptions_per_capita(df, indexing = True):
    
    'Retains only the columns considering only the consumptions levels PER CAPITA'

    
    substring_match_columns = [col for col in df.columns if 'elec_per_capita' in col]

    if indexing:
        exact_match_columns = ['country', 'year', 'iso_code']
        selected_columns = exact_match_columns + substring_match_columns
    else: 
        exact_match_columns = ['year']
        selected_columns = exact_match_columns + substring_match_columns 


    filtered_df = df[selected_columns]

    return filtered_df