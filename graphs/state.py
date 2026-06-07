from typing import TypedDict


class AgentState(TypedDict):

    df: object

    profile: dict

    plan: str

    cleaned_df: object

    validation_issues: list

    report: dict