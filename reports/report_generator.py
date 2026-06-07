import os
import json

import pandas as pd


def save_report(report):

    # Create reports directory
    os.makedirs(
        "reports",
        exist_ok=True
    )

    # Save JSON report
    with open(
        "reports/data_quality_report.json",
        "w"
    ) as f:

        json.dump(
            report,
            f,
            indent=4
        )

    # Save CSV report
    pd.DataFrame(
        [report]
    ).to_csv(
        "reports/data_quality_report.csv",
        index=False
    )

    print(
        "Reports generated successfully"
    )

    print(
        "JSON Report: reports/data_quality_report.json"
    )

    print(
        "CSV Report: reports/data_quality_report.csv"
    )