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
