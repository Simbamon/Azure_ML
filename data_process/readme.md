# Data Processing
This page contains information on how to load and process the data using Apache Spark

## Why Spark 
Data is crucial for machine learning model development as it serves as the foundation for training, validating, and testing models, make predictions, and improve accuracy over time. If you are working with a large dataset, you will need sufficient computing power to handle large set of data in parallel. This repository will focus on using Spark to load raw data and preprocess it into a feasible dataset for machine learning development. In Azure Machine Learning, there are several ways to use Spark for data processing:
- Serverless Spark
- Integrating Azure Synapse Analytics into Azure Machine Learning
- Azure Databricks
- Custom solutions to turn an Azure Machine Learning compute cluster into Spark cluster

### Serverless Spark
Serverless Spark in Azure Machine Learning (AML) Studio is a managed service that allows us to run Apache Spark workloads without needing to manage the underlying infrastructure. Through serverless spark, we can process large-scale data by only focusing on writing and running the Spark jobs and not worrying about cluster management, scaling, or maintenance.

### Integrating Azure Synapse Analytics
You can integrate Azure Synapse Analytics into Azure Machine Learning to streamline data preparation, model training, and deployment. This integration allows us to leverage the massive data processing capabilities of Azure Synapse while move from data ingestion and preparation to model training and deployment in Azure ML, all within the Azure environment.

### Azure Databricks
You can also integrate Azure Databricks to create an environment for data processing, advanced analytics, and machine learning. While Azure Databricks, a managed Apache Spark-based platform, offers data engineering and analytics capabilities, Azure Machine Learning will handle the machine learning side to build an e2e data science workflows.

### Custom Spark Cluster
You can use Azure Machine Learning's compute cluster as a Spark cluster to load and pre-process data. For example, you can read data from ADLS Gen2 and process it using Spark features like PySpark, Pandas, SQL, etc. However, the issue is that AML's compute cluster does not natively support Spark. While the official documentation suggests using Spark clusters managed by Azure (Azure Databricks, Azure Synapse Analytics, Serverless Spark), these options come with additional operational costs and require you to manage separate clusters outside of AML's compute cluster. For an end-to-end machine learning development workflow, it is more efficient to use the existing AML's compute cluster, and you can do that by applying open-source packages like Ray and RayDP.