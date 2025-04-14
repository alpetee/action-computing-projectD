"""
Author: Allie Peterson
Disclaimer: This is showing a misleading story. See the 'Source of Truth' section in the README.
"""

import pandas as pd


def load_and_process_data():
    # Load the data
    df = pd.read_csv('gender.csv')

    # Melt the dataframe to convert year columns to rows
    id_vars = ['Series Name', 'Series Code']
    year_columns = [col for col in df.columns if '[YR' in col]

    df = pd.melt(
        df,
        id_vars=id_vars,
        value_vars=year_columns,
        var_name='Year_Column',
        value_name='Value'
    )

    # Extract year number from the year column (e.g., "1974 [YR1974]" -> 1974)
    df['Year'] = df['Year_Column'].str.extract(r'(\d+)').astype(int)

    # Pivot the Series Name to columns
    df = df.pivot_table(
        index=['Year'],
        columns='Series Name',
        values='Value',
        aggfunc='first'
    ).reset_index()

    # Clean up column names
    df.columns.name = None  # Remove the 'Series Name' label
    df.columns = [col.strip() for col in df.columns]

    # Convert percentage values to numeric and replace NaN with 0
    for col in df.columns:
        if '%' in str(col):
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    return df