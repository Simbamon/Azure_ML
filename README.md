# Azure Machine Learning
This project utilizes Microsoft Azure AI's Machine Learning Studio to streamline the machine learning lifecycle. The goal is to process data, develop machine learning models, deploy them with endpoints, monitor performance, and automate the pipeline for continuous integration and deployment.

## Description
This GitHub repository focuses on how to utilize features in Microsoft Azure Machine Learning (AML) Studio to create an end-to-end machine learning model development pipeline. The workflow includes reading, writing, and cleaning data from Azure Data Lake Storage (ADLS) Gen2 and processing that data within AML Studio to prepare it for model training and testing. Once the model is developed, it can be deployed to the AML workspace (online or batch), and inference calls can be made to generate outcomes. These outcomes will be distributed back to ADLS Gen2 for further data analysis. All these processes will be orchestrated using YAML configurations so that the workflow can be initiated in a Microsoft Azure DevOps environment and follow best practices for DevOps principles.

## Getting Started
Following these instructions will help you set up and run a project for development and testing purposes

### Prerequisites
- Microsoft Azure account
- Azure Machine Learning Studio workspace
- Data (e.g. tabular data like csv) to preprocess and train model

## Azure AI Machine Learning Studio

### Workspace
Work as a central hub for managing all the resources needed for machine learning projects. It includes features to build, train, deploy, and monitor models. Key features of an Azure Machine Learning Workspace include:  
- Resource Management: Centralized management of datasets, experiments, models, and deployments
- Collaboration: Enables team collaboration by sharing resources and facilitating version control
- Compute Management: Manages compute resources such as virtual machines, GPU clusters, and more.

### Feature
 - Components
    - Modularity: Break down complex workflows into manageable parts focused on specific tasks (e.g., data preprocessing, model training, model deployment, etc.).
    - Reusability: Reuse components across multiple pipelines and projects, promoting consistency and reducing repetitive work.
    - Parameterization: Customize component behavior with inputs and parameters.
    - Basic workflow
        - Using YAML file or Python script(SDK v2) to design a component and specify the behavior(e.g., name, type, inputs, outputs, command, etc. ) 
 - Jobs
    - A specific task or set of tasks that run within the Azure ML environment to perform machine learning operations
    - Example jobs:
        - Data Processing Jobs: Cleaning, transforming, and structuring raw data into a format suitable for machine learning
        - Training Jobs: Execute scripts or pipelines to train machine learning models
        - Pipeline Jobs: Run a sequence of steps, each performing a specific function like data preprocessing, model training, or deployment
        - Inference Jobs: Deploy trained models and run them against new data to generate predictions
    - Execution Environment
        - Jobs run on compute resources like AML(Azure Machine Learning) Compute, Kubernetes clusters, or Virtual Machines (VMs)
 - Pipelines
    - Workflow that automates and orchestrates a sequence of steps involved in the machine learning process
    - Example pipelines:
        - Data Preparation: Pipelines can include steps for data ingestion, transformation, and cleaning
        - Model Training: Steps to train models using different algorithms or configurations. These steps can be run in parallel to compare models and select the best one
        - Model Evaluation: Steps to evaluate models based on specific metrics to determine their accuracy and performance
        - Deployment: Deploy models as part of the pipeline, enabling automated model management and updates

## License
This project is licensed under the MIT License - see the LICENSE file for details

## Reference
 - Official Document: [Microsoft Azure Machine Learning Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/?view=azureml-api-2)
 - Github [azureml-examples by Azure](https://github.com/Azure/azureml-examples)
 - Github [MLOps_Workshop by MG-Microsoft](https://github.com/MG-Microsoft/MLOps_Workshop)
 - Github [azure-mlops by datafairy-azure](https://github.com/datafairy-azure/azure-mlops)