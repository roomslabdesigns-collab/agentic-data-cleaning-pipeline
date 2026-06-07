from ingestion.loader import load_data


df = load_data(
    "datasets/raw/employees.csv"
)

print(df.head())