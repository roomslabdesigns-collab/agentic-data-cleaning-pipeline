import pandas as pd


def clean_data(
    df,
    plan
):

    # Remove duplicates
    if plan.get(
        "remove_duplicates",
        False
    ):
        df = df.drop_duplicates()

    # Missing value strategy
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

    # Outlier handling
    outlier_strategy = plan.get(
        "outlier_strategy",
        "none"
    )

    if outlier_strategy == "remove":

        if "Age" in df.columns:

            df = df[
                (df["Age"] >= 0)
                &
                (df["Age"] <= 120)
            ]

    # Category standardization
    if plan.get(
        "standardize_categories",
        False
    ):

        if "Gender" in df.columns:

            gender_map = {
                "m": "Male",
                "male": "Male",
                "f": "Female",
                "female": "Female"
            }

            df["Gender"] = (
                df["Gender"]
                .astype(str)
                .str.lower()
                .map(gender_map)
                .fillna(df["Gender"])
            )

    return df