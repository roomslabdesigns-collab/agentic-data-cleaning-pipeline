from langgraph.graph import (
    StateGraph,
    END
)

from graphs.state import AgentState

from agents.profiling_agent import (
    profile_data
)

from agents.planning_agent import (
    create_cleaning_plan
)

from agents.cleaning_agent import (
    clean_data
)

from agents.validation_agent import (
    validate_data
)

from agents.report_agent import (
    generate_report
)


# PROFILING NODE
def profiling_node(state):

    profile = profile_data(
        state["df"]
    )

    return {
        "profile": profile
    }


# PLANNING NODE
def planning_node(state):

    plan = create_cleaning_plan(
        state["profile"]
    )

    return {
        "plan": plan
    }


# CLEANING NODE
def cleaning_node(state):

    cleaned_df = clean_data(
    state["df"],
    state["plan"]
    )

    return {
        "cleaned_df": cleaned_df
    }


# VALIDATION NODE
def validation_node(state):

    issues = validate_data(
        state["cleaned_df"]
    )

    return {
        "validation_issues": issues
    }


# REPORT NODE
def report_node(state):

    report = generate_report(
        state["df"],
        state["cleaned_df"],
        state["profile"],
        state["validation_issues"]
    )

    return {
        "report": report
    }


# BUILD WORKFLOW
workflow = StateGraph(
    AgentState
)

workflow.add_node(
    "profiling",
    profiling_node
)

workflow.add_node(
    "planning",
    planning_node
)

workflow.add_node(
    "cleaning",
    cleaning_node
)

workflow.add_node(
    "validation",
    validation_node
)

workflow.add_node(
    "report",
    report_node
)

workflow.set_entry_point(
    "profiling"
)

workflow.add_edge(
    "profiling",
    "planning"
)

workflow.add_edge(
    "planning",
    "cleaning"
)

workflow.add_edge(
    "cleaning",
    "validation"
)

workflow.add_edge(
    "validation",
    "report"
)

workflow.add_edge(
    "report",
    END
)

graph = workflow.compile()