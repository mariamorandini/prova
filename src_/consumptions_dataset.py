import pandas as pd
def retain_consumptions(df):
    
    'Retains only the columns considering only the consumptions levels'

    exact_match_columns = ['country', 'year', 'iso_code']
    substring_match_columns = [col for col in df.columns if 'consumption' in col]

    selected_columns = exact_match_columns + substring_match_columns

    filtered_df = df[selected_columns]

    return filtered_df
