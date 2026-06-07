import json

from ollama import Client


client = Client(
    host="http://127.0.0.1:11434"
)


def create_cleaning_plan(profile):

    prompt = f"""
You are a data quality expert.

Based on the profiling report,
create a cleaning plan.

Profiling Report:

{json.dumps(profile, indent=2)}

Return only the cleaning actions.
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

    return response["message"]["content"]