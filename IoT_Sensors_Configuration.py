# IoT_Sensors_Configuration.py
"""
Script for loading IoT sensor configuration.
"""

import json

def load_sensor_config(config_file='IoT_Sensors_Configuration.json'):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config
