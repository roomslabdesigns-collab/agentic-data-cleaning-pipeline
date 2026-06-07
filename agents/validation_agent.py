import pandas as pd


def validate_data(df):

    issues = []

    if "Age" in df.columns:

        invalid_age = df[
            (df["Age"] < 0)
            | (df["Age"] > 120)
        ]

        if not invalid_age.empty:

            issues.append(
                f"Found {len(invalid_age)} invalid age values."
            )

    if df.isnull().sum().sum() > 0:

        issues.append(
            "Dataset still contains missing values."
        )

    return issues