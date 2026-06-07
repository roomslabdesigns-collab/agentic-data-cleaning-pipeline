from ingestion.loader import load_data

from graphs.workflow import graph

from reports.report_generator import (
    save_report
)


df = load_data(
    "datasets/raw/employees.csv"
)

result = graph.invoke(
    {
        "df": df
    }
)

save_report(
    result["report"]
)

print(
    result["report"]
)