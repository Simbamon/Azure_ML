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

For this repository, we will set up a Ray cluster using the [Ray-on-AML](https://github.com/microsoft/ray-on-aml) open-source Python package and use the [RayDP](https://github.com/oap-project/raydp) open-source Python package to establish our own Spark cluster.

- Ray: Distributed system framework that allows you to scale Python applications across multiple nodes (compute clusters) for parallel computing.

- Ray-on-AML: Developed by Microsoft. Unfortunately, as of today (October 18, 2024), the last update for Ray-on-AML was on December 15, 2022. If you try to use the interactive mode of Ray-on-AML, there is an issue with the incompatible packages that prevent you from using Ray on AML's compute cluster. However, when using AML's job, the Ray features are still available, allowing you to distribute data loading and processing tasks across multiple nodes.

- RayDP: Open-source Python library. It is a library for distributed data processing, built on top of Ray and Apache Spark. With this library, you can integrate Spark for large-scale data processing with Ray's distributed computing capabilities. This repository uses RayDP version 1.6.1 and Spark version 3.5.1 in a Docker image to set up a Spark cluster environment on AML's compute cluster.

- Environment setup  
In this repository, this page will include information about setting up custom Docker images, the Conda environment, and other necessary configurations to set up a customized Spark cluster on AML's compute cluster.  
Refer to the `./custom_spark/env_setup` directory for more information.

### Azure Machine Learning Filesystem
Python library built on top of Azure ADLS Gen2 that specifically deals with filesystem operation. This repository will include an use case that requires retrieving all directories from ADLS Gen2 containing table data. If you already have ADLS Gen2 set as a datastore in AML Studio, you can use `azureml.fsspec.spec.azuremachinelearningfilesystem` to locate all the necessary directories for the use case.

```python
from azureml.fsspec import AzureMachineLearningFileSystem

adls_path = 'azureml://subscriptions/<YOUR_SUBSCRIPTION_ID>/resourcegroups/<YOUR_RESOURCE_GROUP>/workspaces/<YOUR_WORKSPACE_NAME>/datastore/datastorename
fs = AzureMachineLearningFileSystem(adls_path)
fs_list = fs.ls()
```