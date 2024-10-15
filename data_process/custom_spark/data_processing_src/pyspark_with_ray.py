import subprocess
import ray
from ray_on_aml.core import Ray_On_AML
import raydp

def testing() -> None:
    print("printing ray version...")
    ray_version = subprocess.run("ray --version", shell=True, capture_output=True)

def main() -> None:
    # Your data processing function goes here
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