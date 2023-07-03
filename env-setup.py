import os
import subprocess
import sys
import re


def create_or_verify_conda_environment(env_file_path, environment_name):
    # Check if the environment file exists
    if not os.path.exists(env_file_path):
        print(f"Environment file '{env_file_path}' does not exist.")
        sys.exit(1)

    pattern = re.compile(f"(?<=name: ){environment_name}")
    # Read the environment file
    with open(env_file_path, "r") as f:
        env_data = f.read()
    # breakpoint()
    env_name = re.findall(pattern=pattern, string=env_data)[0]

    # Check if the environment is already created
    process = subprocess.Popen(["conda", "info", "--envs"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    output_str = output.decode("utf-8")

    if env_name in output_str:
        print(f"Environment '{env_name}' already exists.")
        return

    # Create the environment
    print(f"Creating environment '{env_name}'...")
    process = subprocess.Popen(["conda", "env", "create", "-f", env_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Check the process return code
    if process.returncode == 0:
        print(f"Environment '{env_name}' created successfully.")
    else:
        print(f"Failed to create environment '{env_name}'.")
        print(error.decode("utf-8"))
        sys.exit(1)


# Specify the path to your environment.yml file
env_file = "environment.yml"
environment_name = "web-scraper"

create_or_verify_conda_environment(env_file, environment_name)