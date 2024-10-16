import subprocess
import ray
from ray_on_aml.core import Ray_On_AML
import raydp

def data_processing() -> None:
    spark = raydp.init_spark(app_name='RayDP spark cluster',
                         num_executors=2,
                         executor_cores=2,
                         executor_memory='4GB')

def testing() -> None:
    print("printing ray version...")
    ray_version = subprocess.run("ray --version", shell=True, capture_output=True)

def main() -> None:
    # Your data processing function goes herewd
    testing()

if __name__ == "__main__":
    ray_on_aml = Ray_On_AML()
    ray = ray_on_aml.getRay()
    if ray:
        print("head node detected")
        ray.init(address="auto")
        main()
    
    else:
        print("This node is a worker node")