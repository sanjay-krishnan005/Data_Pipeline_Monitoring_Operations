# Architecture Overview

## Data Pipeline Architecture

```mermaid
flowchart LR
    Raw[Raw Data Storage] --> Databricks[Databricks Transformation]
    Databricks --> Processed[Processed Data Storage]
    Processed --> SQL[SQL Analytics & Validation]
    Databricks --> Monitor[Pipeline Monitor & Alerting]
    Monitor --> Incidents[Incident Management]
```

### Components
- **Data Ingestion (`data/raw/`)**: Source landing zone for raw incoming datasets.
- **Data Transformation (`databricks/transformation.py`)**: Spark / Databricks transformation notebooks and scripts.
- **Data Processing (`data/processed/`)**: Refined and curated data outputs.
- **Validation & Analytics (`sql/`)**: SQL data quality checks and analytical queries.
- **Pipeline Monitoring (`monitoring/pipeline_monitor.py`)**: Pipeline health checks, metrics, and alerts.
- **Incidents (`incidents/`)**: Post-mortems, alerts, and incident tracking records.
