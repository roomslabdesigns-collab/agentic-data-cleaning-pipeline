import json

from ollama import Client


client = Client(
    host="http://127.0.0.1:11434"
)


def create_cleaning_plan(profile):

    prompt = f"""
You are a data cleaning expert.

Based on the dataset profile below,
return ONLY valid JSON.

Example:

{{
    "remove_duplicates": true,
    "missing_strategy": "median",
    "outlier_strategy": "remove",
    "standardize_categories": true
}}

Profile:

{json.dumps(profile, indent=2)}
"""

    response = client.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    try:

        return json.loads(
            response["message"]["content"]
        )

    except:

        return {
            "remove_duplicates": True,
            "missing_strategy": "median",
            "outlier_strategy": "remove",
            "standardize_categories": True
        }