from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import argparse
import mltable

parser = argparse.ArgumentParser()
parser.add_argument("--input_data", help="Path to input data")

args = parser.parse_args()
adls_directory = args.input_data

print(adls_directory)

## read all the csv files
path = [
    {
        'pattern': adls_directory + '*.csv'
    }
]

tbl = mltable.from_delimited_files(paths=path)

tbl.show()

tbl.save(path='./tmp', overwrite=True)

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

data_with_version = Data(
    path='./tmp',
    type=AssetTypes.MLTABLE,
    description="Tetsting with pipeline asset management",
    name="greenTaxiData_asset_mgmt",
)

ml_client.data.create_or_update(data_with_version)