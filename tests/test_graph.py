from ingestion.loader import load_data

from graphs.workflow import graph


df = load_data(
    "datasets/raw/employees.csv"
)

result = graph.invoke(
    {
        "df": df
    }
)

print("\nPLAN:")
print(result["plan"])

print("\nREPORT:")
print(result["report"])