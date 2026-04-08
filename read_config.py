import json


def read_config(config_path):
    with open(config_path, "r") as f:
        config = json.load(f)
    return config


def get_output_folder(config):
    return f"{config['outputs']['root_dir']}/{config['outputs']['run_name']}"
