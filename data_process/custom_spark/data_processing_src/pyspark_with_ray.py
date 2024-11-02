import subprocess
import ray
from ray_on_aml.core import Ray_On_AML
import raydp
import argparse

def data_processing(input_path: str) -> None:
    spark = raydp.init_spark(app_name='RayDP spark cluster',
                         num_executors=2,
                         executor_cores=2,
                         executor_memory='4GB')

    print("dcalling spark version...")
    print(spark.version)

    data = [("sample1", 10), ("sample2", 15), ("sample3", 20)]
    sample_df = spark.createDataFrame(data, ["sample", "number"])

    data_from_spark = spark.read.format('parquet').option('recursiveFileLookup', 'true').option('header', 'true').load(input_path)

def testing() -> None:
    print("printing ray version...")
    ray_version = subprocess.run("ray --version", shell=True, capture_output=True)

def main() -> None:
    testing()

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", help="input path")
    args = parser.parse_args()
    input_path = args.input_path

    data_processing(input_path)

if __name__ == "__main__":
    ray_on_aml = Ray_On_AML()
    ray = ray_on_aml.getRay()
    if ray:
        print("head node detected")
        ray.init(address="auto")
        main()
    
    else:
        print("This node is a worker node")