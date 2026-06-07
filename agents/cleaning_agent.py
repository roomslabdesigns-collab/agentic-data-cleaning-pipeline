import pandas as pd


def clean_data(
    df,
    plan
):

    if plan.get(
        "remove_duplicates",
        False
    ):
        df = df.drop_duplicates()

    strategy = plan.get(
        "missing_strategy",
        "median"
    )

    numeric_cols = df.select_dtypes(
        include=["number"]
    ).columns

    for col in numeric_cols:

        if strategy == "mean":

            value = df[col].mean()

        else:

            value = df[col].median()

        df[col] = df[col].fillna(
            value
        )

    return df