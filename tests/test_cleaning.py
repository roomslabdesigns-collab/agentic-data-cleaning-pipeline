from ingestion.loader import load_data

from agents.cleaning_agent import (
    clean_data
)


df = load_data(
    "datasets/raw/employees.csv"
)

print("Before Cleaning")
print(df)

cleaned_df = clean_data(df)

print("\nAfter Cleaning")
print(cleaned_df)