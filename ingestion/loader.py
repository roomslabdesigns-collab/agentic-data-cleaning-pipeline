import pandas as pd

import sqlite3


def load_data(
    source
):

    # CSV
    if source.endswith(".csv"):

        return pd.read_csv(
            source
        )

    # Excel
    elif (
        source.endswith(".xlsx")
        or
        source.endswith(".xls")
    ):

        return pd.read_excel(
            source,
            engine="openpyxl"
        )

    else:

        raise ValueError(
            "Unsupported file format"
        )


def load_from_database(
    db_path,
    table_name
):

    conn = sqlite3.connect(
        db_path
    )

    df = pd.read_sql_query(
        f"SELECT * FROM {table_name}",
        conn
    )

    conn.close()

    return df