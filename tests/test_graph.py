from ingestion.loader import load_data

import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from graphs.workflow import graph
from ingestion.loader import load_data


df = load_data(
    "datasets/raw/employees.csv"
)

result = graph.invoke(
    {
        "df": df
    }
)

print(result["report"])