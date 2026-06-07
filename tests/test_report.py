from ingestion.loader import load_data

from agents.profiling_agent import profile_data
from agents.cleaning_agent import clean_data
from agents.validation_agent import validate_data
from agents.report_agent import generate_report


df = load_data(
    "datasets/raw/employees.csv"
)

profile = profile_data(df)

cleaned_df = clean_data(df)

issues = validate_data(
    cleaned_df
)

report = generate_report(
    df,
    cleaned_df,
    profile,
    issues
)

print(report)