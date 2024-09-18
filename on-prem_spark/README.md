# On-Prem Spark
This on-premises Spark cluster (Docker) is intended for testing your Spark jobs, instead of relying on services like Azure Synapse, a serverless Spark cluster, or Azure Databricks. 

## Installation
- To run the Spark cluster locally, you can follow one of the instructions defined in the Makefile (`run-scaled`)
    - This will build and start 5 containers for your local Spark cluster: 1 master, 3 workers, and 1 history node
    ```bash
    run-scaled
    ```

## Reference
- Medium Article: [Setting up a Spark standalone cluster on Docker in layman terms by Marin Aglić](https://medium.com/@MarinAgli1/setting-up-a-spark-standalone-cluster-on-docker-in-layman-terms-8cbdc9fdd14b)