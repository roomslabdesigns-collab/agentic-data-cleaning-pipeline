from ingestion.loader import load_data

from agents.profiling_agent import (
    profile_data
)

from agents.planning_agent import (
    create_cleaning_plan
)


df = load_data(
    "datasets/raw/employees.csv"
)

profile = profile_data(df)

plan = create_cleaning_plan(
    profile
)

print(plan)