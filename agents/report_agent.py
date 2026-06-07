def generate_report(
    original_df,
    cleaned_df,
    profile,
    validation_issues
):

    report = {
        "original_rows": len(original_df),
        "cleaned_rows": len(cleaned_df),
        "duplicates_found": profile["duplicates"],
        "missing_values": profile["missing_values"],
        "validation_issues": validation_issues
    }

    return report