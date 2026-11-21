import os
from configparser import ConfigParser

def read_configuration(category,key):
    config=ConfigParser()
    root_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path=os.path.join(root_dir,"config","config.ini")
    config.read(config_path)
    return config.get(category,key)