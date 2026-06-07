import pandas as pd


def profile_data(df):

    profile = {}

    profile["rows"] = len(df)

    profile["columns"] = len(df.columns)

    profile["column_names"] = list(
        df.columns
    )

    profile["missing_values"] = (
        df.isnull()
        .sum()
        .to_dict()
    )

    profile["duplicates"] = int(
        df.duplicated().sum()
    )

    profile["data_types"] = (
        df.dtypes
        .astype(str)
        .to_dict()
    )

    return profile