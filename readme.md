# Agentic AI Data Quality Platform

> **What if data cleaning wasn't a fixed set of preprocessing rules, but a system that could first understand the dataset, decide what it needs, and then validate the result?**

The **Agentic AI Data Quality Platform** is a multi-agent data quality system that automates the workflow from raw structured data to a validated, report-ready dataset.

Instead of applying the same preprocessing rules to every dataset, the system first **profiles the data**, uses an LLM-powered **Planning Agent** to determine which cleaning actions are appropriate, executes the generated plan through a **Cleaning Agent**, validates the result, and produces a structured quality report.

The current prototype supports **CSV, Excel, and SQLite** data sources and uses **LangGraph** to orchestrate the workflow.

---

## How It Works

```text
CSV / Excel / SQLite
        │
        ▼
 Data Ingestion
        │
        ▼
 Profiling Agent
        │
        │ Dataset Profile
        ▼
 Planning Agent
  (Ollama + Qwen3)
        │
        │ Cleaning Plan
        ▼
 Cleaning Agent
        │
        ├── Missing Values
        ├── Duplicates
        ├── Outliers
        └── Categories
        │
        ▼
 Validation Agent
        │
        ▼
 Report Agent
        │
        ├── JSON Report
        └── CSV Report
        │
        ▼
 Validated Dataset
```

### Core Design

The key architectural decision is the separation of **decision-making from execution**:

```text
Dataset Profile
      ↓
AI-Generated Cleaning Plan
      ↓
Cleaning Agent
      ↓
Validation Agent
      ↓
Validated Dataset
```

The AI is responsible for deciding **what should be done**. The Cleaning Agent is responsible for **executing the selected operations**.

This makes the workflow easier to reason about and extend than a single script containing all cleaning logic.

---

# The Problem

Traditional data-cleaning workflows often depend on manually inspecting datasets and applying predefined preprocessing rules.

A typical workflow looks like:

```text
Raw Dataset
     ↓
Manual Inspection
     ↓
Write Cleaning Rules
     ↓
Run Preprocessing
     ↓
Check Results
     ↓
Generate Report
```

The problem is that datasets do not always require the same treatment.

For example:

* Missing values may require different strategies.
* Duplicate records may need to be removed.
* Numerical values may contain invalid observations.
* Categorical values may appear as `M`, `male`, and `MALE`.
* Different data sources require different ingestion workflows.

The result is a repetitive process where the cleaning logic is often defined **before the system fully understands the dataset**.

---

# The Agentic Approach

The platform changes the workflow from:

> **Fixed rules → Clean data**

to:

> **Understand data → Decide → Execute → Validate → Report**

### 1. Ingest

Load structured data from:

* CSV
* Excel
* SQLite

### 2. Profile

The **Profiling Agent** analyzes the dataset and produces a structured profile containing:

* Number of rows and columns
* Data types
* Missing values
* Duplicate records
* Dataset quality information

### 3. Plan

The **Planning Agent** receives the profile and uses an LLM to generate a structured cleaning strategy.

Example:

```json
{
  "remove_duplicates": true,
  "missing_strategy": "median",
  "outlier_strategy": "remove",
  "standardize_categories": true
}
```

### 4. Execute

The **Cleaning Agent** reads the generated plan and performs the selected operations using Pandas.

Supported operations include:

* Missing-value handling
* Duplicate removal
* Outlier handling
* Category standardization

### 5. Validate

The **Validation Agent** checks the cleaned dataset for remaining data-quality issues.

The system does not assume that successful execution means successful cleaning.

### 6. Report

The **Report Agent** generates structured reports containing:

* Original dataset information
* Cleaning results
* Validation issues
* Quality metrics
* Quality score

Reports are exported as:

* JSON
* CSV

---

# Example

The prototype was tested on a dataset containing **6 rows and 4 columns**.

Initial issues included:

```text
Rows:               6
Columns:            4
Duplicates:         1
Missing Age:       1
Missing Salary:    1
Invalid Age:      150
```

The Planning Agent generated:

```text
Remove duplicates      → True
Missing strategy       → Median
Outlier strategy       → Remove
Category standardize   → True
```

The Cleaning Agent then executed the plan.

Result:

```text
Original rows:      6
Cleaned rows:       4
Duplicates found:   1
Validation issues:  []
```

The important part is not the specific quality score. The important part is that the cleaning behavior was determined by an **AI-generated plan** and then checked through a separate **validation stage**.

---

# Agent Architecture

| Agent                | Responsibility                                        |
| -------------------- | ----------------------------------------------------- |
| **Profiling Agent**  | Understands the dataset and identifies quality issues |
| **Planning Agent**   | Generates an AI-driven cleaning strategy              |
| **Cleaning Agent**   | Executes the selected cleaning operations             |
| **Validation Agent** | Checks the cleaned dataset for remaining issues       |
| **Report Agent**     | Generates quality reports and metrics                 |

**LangGraph** coordinates the complete agent workflow.

---

# Key Features

### Multi-Agent Workflow

* Profiling Agent
* LLM-powered Planning Agent
* Cleaning Agent
* Validation Agent
* Report Agent
* LangGraph orchestration

### Data Ingestion

* CSV files
* Excel spreadsheets
* SQLite databases

### Data Cleaning

* Missing-value handling
* Duplicate removal
* Outlier handling
* Category standardization

### Validation & Reporting

* Automated validation
* Dataset comparison
* Quality metrics
* JSON reports
* CSV reports

---

# Technology Stack

| Category            | Technology    |
| ------------------- | ------------- |
| Language            | Python        |
| Data Processing     | Pandas, NumPy |
| Agent Orchestration | LangGraph     |
| LLM Runtime         | Ollama        |
| LLM                 | Qwen3 4B      |
| Database            | SQLite        |
| Excel Processing    | OpenPyXL      |
| Reporting           | JSON, CSV     |

---

# Product Thinking & Tradeoffs

### LLM-generated plans can be wrong

The Planning Agent may select an unsuitable cleaning strategy.

**Mitigation:** The output is constrained to structured JSON and the resulting dataset passes through a separate validation stage.

### Removing data can cause information loss

An outlier may represent a legitimate observation rather than an error.

**Current approach:** The prototype uses explicit cleaning strategies for known invalid values.

**Future approach:** Add configurable thresholds and human approval for higher-risk transformations.

### Quality scores can be misleading

The current prototype's quality score is based on the proportion of remaining rows. It should therefore not be interpreted as a complete measure of statistical or semantic data quality.

A production version should combine multiple quality dimensions.

---

# Current State

### Implemented

* CSV ingestion
* Excel ingestion
* SQLite ingestion
* Dataset profiling
* LLM-powered cleaning plans
* Automated cleaning
* Validation
* LangGraph orchestration
* Missing-value handling
* Duplicate removal
* Outlier handling
* Category standardization
* JSON reporting
* CSV reporting

### Future Extensions

* FastAPI deployment
* Streamlit interface
* PostgreSQL integration
* Docker deployment
* Human approval workflow
* Advanced LLM-based category normalization
* Persistent data-quality monitoring

These are future extensions, not part of the current prototype.

---

# What Makes It Agentic?

The project is not simply a Pandas preprocessing script.

The key difference is:

```text
Traditional Pipeline

Fixed Rules
     ↓
Clean
     ↓
Validate
```

versus:

```text
Agentic Pipeline

Understand Dataset
        ↓
AI Generates Plan
        ↓
Execute Plan
        ↓
Validate Result
        ↓
Generate Report
```

The system uses the LLM as a **decision layer**, while deterministic Python code performs the actual data transformations.

That separation combines **LLM-based decision making with traditional data-processing techniques** to create a more structured and controllable agentic workflow.
