import pandas as pd


def clean_data(df):

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing numeric values
    numeric_cols = df.select_dtypes(
        include=["number"]
    ).columns

    for col in numeric_cols:

        median_value = df[col].median()

        df[col] = df[col].fillna(
            median_value
        )

    return df