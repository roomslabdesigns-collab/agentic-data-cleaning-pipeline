from ingestion.loader import load_data

from agents.profiling_agent import (
    profile_data
)

df = load_data(
    "datasets/raw/employees.csv"
)

profile = profile_data(df)

print(profile)