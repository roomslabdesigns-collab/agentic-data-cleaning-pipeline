from ingestion.loader import load_data


df = load_data(
    "datasets/raw/employees.xlsx"
)

print(df.head())