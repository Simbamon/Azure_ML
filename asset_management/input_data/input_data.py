from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input_data", help="Path to input data")

args = parser.parse_args()
adls_input_data = args.input_data

print(adls_input_data)

subscription_id= "<YOUR_SUBSCRIPTION_ID>"
resource_group_name= "<YOUR_RESOURCE_GROUP_NAME>"
workspace_name= "<YOUR_WORKSPACE_NAME>"

ml_client = MLClient(
    DefaultAzureCredential(),
    subscription_id,
    resource_group_name,
    workspace_name
)

# ml_client = MLClient.from_config(DefaultAzureCredential())

data_path = adls_input_data

data_with_version = Data(
    path=data_path,
    type=AssetTypes.URI_FILE,
    description="Tetsting with pipeline asset management",
    name="greenTaxiData_asset_mgmt",
)

ml_client.data.create_or_update(data_with_version)