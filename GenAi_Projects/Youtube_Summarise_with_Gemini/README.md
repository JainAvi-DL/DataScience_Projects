📌 Project Overview
This project demonstrates a comprehensive data engineering pipeline built on Microsoft Azure to process and analyze the Tokyo Olympics 2021 dataset. The goal was to migrate raw data from an external source (AWS S3), transform it into a structured format, and derive actionable business insights using modern cloud-native tools.


🏗️ Architecture & Data Flow
The pipeline follows a modern data warehouse architecture:

Ingestion: Data is ingested from Amazon S3 into Azure Blob Storage using Azure Data Factory (ADF).

Transformation: Raw data is processed and cleaned within Azure Databricks using Spark.

Analytics: Business logic is applied via Spark SQL to identify trends in athlete participation and regional performance.


🛠️ Tech Stack
Source: Amazon S3 (Simulated external provider)

Orchestration: Azure Data Factory (ADF)

Storage: Azure Blob Storage (Data Lake)

Compute/Transformation: Azure Databricks (Apache Spark)

Languages: SQL, Python (PySpark)

🚀 Key Features & Implementation
1. Data Ingestion (ADF)
Established connectivity between AWS and Azure using Linked Services and IAM credentials.

Configured a Copy Activity in ADF to automate the transfer of CSV/Excel files from S3 buckets to Azure Blob containers.

2. Data Transformation (Databricks)
Mounting Storage: Connected the Azure Storage Account to the Databricks File System (DBFS) for seamless data access.

Schema Enforcement: Defined schemas for various datasets (Athletes, Coaches, Entries by Gender).

Cleaning: Handled missing values and performed column normalization (e.g., removing special characters/spaces from headers) to ensure SQL compatibility.

3. Business Insights (Spark SQL)
Transformed raw data into a relational format to answer key questions:

Regional Performance: Analyzing which regions produced the most profitable or successful outcomes.

Gender Distribution: Evaluating the participation ratio across different sporting disciplines.

Resource Allocation: Identifying top-performing states/cities based on total medal/participation counts.


📈 Key Achievements
Successfully implemented a cross-cloud migration strategy (AWS to Azure).

Automated data movement, reducing manual handling and potential for error.

Transformed unstructured "bronze" layer data into a "gold" layer ready for visualization and reporting.
