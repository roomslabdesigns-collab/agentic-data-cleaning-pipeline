# Agentic AI-Powered Data Cleaning Pipeline

**Agentic AI-Powered Data Cleaning Pipeline** is an agent-based data quality platform that automates the process of preparing structured datasets for analysis. Instead of relying only on fixed preprocessing rules, the system uses an LLM-powered **Planning Agent** to analyze the dataset profile and generate a cleaning strategy, which is then executed and validated by downstream agents.

The pipeline accepts data from **CSV files, Excel spreadsheets, and SQLite databases**. After ingestion, the **Profiling Agent** examines the dataset to identify missing values, duplicate records, data types, and potential quality issues. The **Planning Agent**, powered by Ollama and Qwen3 4B, converts this profile into a structured cleaning plan covering operations such as missing-value handling, duplicate removal, outlier treatment, and categorical standardization.

The generated plan is passed to the **Cleaning Agent**, which applies the selected transformations using Pandas. A **Validation Agent** then checks the resulting dataset for remaining quality issues. Finally, the **Report Agent** compares the original and cleaned datasets and generates machine-readable **JSON and CSV reports** containing cleaning results and quality metrics.

The workflow is orchestrated using **LangGraph**, creating a clear separation between analysis, decision-making, execution, validation, and reporting. This design demonstrates how LLMs can be used as a decision layer within traditional data engineering and preprocessing workflows rather than directly modifying data without validation.

### Architecture

```text
CSV / Excel / SQLite
        │
        ▼
  Data Ingestion
        │
        ▼
  Profiling Agent
        │
        │  Dataset profile
        ▼
  Planning Agent
  (Ollama + Qwen3 4B)
        │
        │  Cleaning plan
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
   Cleaned Dataset
```

### Key Features

**Agent-Based Data Quality Workflow**

* Dataset profiling and quality assessment
* LLM-generated cleaning strategy
* Automated execution of the generated plan
* Post-cleaning validation
* Structured quality reporting

**Data Ingestion**

* CSV files
* Excel spreadsheets
* SQLite databases

**Data Cleaning**

* Missing-value handling
* Duplicate removal
* Outlier handling
* Categorical value standardization

**Validation & Reporting**

* Validation of the cleaned dataset
* Original vs. cleaned dataset comparison
* JSON quality reports
* CSV quality reports
* Dataset quality metrics

### Technology Stack

* **Python** — Core implementation
* **Pandas** — Data processing and transformation
* **LangGraph** — Agent workflow orchestration
* **Ollama** — Local LLM inference
* **Qwen3 4B** — Planning Agent
* **SQLite** — Database ingestion
* **OpenPyXL** — Excel processing
* **NumPy** — Numerical operations
