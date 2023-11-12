import configparser
import os
import sys

from dataset import get_pool_dataset


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Invalid command")
        exit(1)

    # Get the absolute path of the current script
    script_path = os.path.abspath(__file__)

    # Get the directory containing the script
    script_dir = os.path.dirname(script_path)

    # Specify the name of your INI configuration file
    config_file_name = "config.ini"

    # Build the absolute path to the configuration file
    config_file_path = os.path.join(script_dir, config_file_name)

    # Create ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read(config_file_path)

    # Access the configuration values
    host = config.get('general', 'host')
    auth = config.get('general', 'auth')

    if sys.argv[1] == 'get_pool_dataset':
        get_pool_dataset(host, auth)
