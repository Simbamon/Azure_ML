# Azure Machine Learning
This project utilizes Microsoft Azure AI's Machine Learning Studio to streamline the machine learning lifecycle. The goal is to process data, develop machine learning models, deploy them with endpoints, monitor performance, and automate the pipeline for continuous integration and deployment.

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
    - Basic workflow:
        - Using YAML file or Python script(SDK v2) to design a component and specify the behavior(e.g., name, type, inputs, outputs, command, etc. ) 