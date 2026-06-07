import pandas as pd

import sqlite3


df = pd.read_csv(
    "datasets/raw/employees.csv"
)

conn = sqlite3.connect(
    "database/employees.db"
)

df.to_sql(
    "employees",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print(
    "Database created successfully"
)