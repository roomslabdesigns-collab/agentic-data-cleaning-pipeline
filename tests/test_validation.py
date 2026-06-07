from ingestion.loader import load_data

from agents.cleaning_agent import (
    clean_data
)

from agents.validation_agent import (
    validate_data
)


df = load_data(
    "datasets/raw/employees.csv"
)

cleaned_df = clean_data(df)

issues = validate_data(
    cleaned_df
)

print(issues)