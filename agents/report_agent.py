def generate_report(
    original_df,
    cleaned_df,
    profile,
    validation_issues
):

    original_rows = len(
        original_df
    )

    cleaned_rows = len(
        cleaned_df
    )

    quality_score = round(
        (cleaned_rows / original_rows) * 100,
        2
    )

    report = {
        "original_rows": original_rows,
        "cleaned_rows": cleaned_rows,
        "quality_score": quality_score,
        "duplicates_found": profile["duplicates"],
        "missing_values": profile["missing_values"],
        "validation_issues": validation_issues
    }

    return report