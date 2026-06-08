# Agentic AI-Powered Data Cleaning Pipeline

Agentic AI-Powered Data Cleaning Pipeline is a multi-agent data quality platform designed to automate the process of profiling, cleaning, validating, and reporting on structured datasets. The system combines LangGraph-based agent orchestration, LLM-powered decision making through Ollama, and automated data preprocessing techniques to improve data quality with minimal human intervention. The platform supports data ingestion from CSV files, Excel spreadsheets, and SQLite databases. Once a dataset is loaded, the Profiling Agent analyzes dataset statistics, data types, missing values, duplicates, and overall data quality issues. The Planning Agent uses an LLM to generate a structured cleaning strategy based on the profiling results. The Cleaning Agent executes the generated plan by handling missing values, removing duplicates, standardizing categorical values, and removing outliers. The Validation Agent verifies the quality of the cleaned dataset and identifies any remaining issues, while the Report Agent generates detailed data quality reports in JSON and CSV formats along with a quality score. The project is built using Python, Pandas, LangGraph, Ollama, SQLite, and OpenPyXL, demonstrating concepts such as Agentic AI, multi-agent workflows, intelligent data preprocessing, automated data quality management, workflow orchestration, and data engineering pipelines. The architecture is designed to be extensible and can be enhanced with FastAPI deployment, Streamlit dashboards, PostgreSQL integration, Docker containerization, advanced LLM-driven standardization, and enterprise-scale data quality monitoring.

Data Sources (CSV / Excel / SQLite Database)
│
▼
Data Ingestion Agent
│
▼
Profiling Agent
│
▼
Planning Agent
│
▼
LangGraph Workflow
│
├── Missing Value Strategy
│
├── Duplicate Removal Strategy
│
├── Outlier Handling Strategy
│
└── Category Standardization Strategy
│
▼
Cleaning Agent
│
▼
Validation Agent
│
▼
Report Agent
│
├── JSON Report Generation
│
├── CSV Report Generation
│
└── Quality Score Calculation
│
▼
Clean Dataset

#**Features**

#**Multi-Agent Architecture**
Profiling Agent for dataset analysis and quality assessment
Planning Agent for AI-driven cleaning strategy generation
Cleaning Agent for automated data preprocessing
Validation Agent for data quality verification
Report Agent for quality reporting and analytics
LangGraph workflow for agent orchestration

#**Data Ingestion**
CSV file support
Excel file support
SQLite database support
Automated dataset loading and preprocessing

#**Data Quality Management**
Missing value detection and handling
Duplicate record detection and removal
Outlier detection and removal
Categorical data standardization
Data validation and quality scoring

#**Reporting System**
JSON report generation
CSV report generation
Dataset quality metrics
Automated data quality summaries

#**Technology Stack**
Python
Pandas
LangGraph
Ollama
Qwen 3 4B
SQLite
OpenPyXL
NumPy
