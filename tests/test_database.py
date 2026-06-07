from ingestion.loader import (
    load_from_database
)


df = load_from_database(
    "database/employees.db",
    "employees"
)

print(df)