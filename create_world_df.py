import pandas as pd 

def create_world_df(df):

    'Output: dataset aggregated over countries, separated by years '


    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df_numeric = df.select_dtypes(include='number')
    world_df = df_numeric.groupby('year').sum().reset_index()


    csv_path = 'world_df.csv'
    world_df.to_csv(csv_path, index=False)

    return None
