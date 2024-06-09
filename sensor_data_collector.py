# sensor_data_collector.py
"""
Script for collecting data from smart sensors.
"""

import json
import random
import time

class SensorDataCollector:
    def __init__(self, config_file='IoT_Sensors_Configuration.json'):
        with open(config_file, 'r') as file:
            self.config = json.load(file)

    def collect_data(self):
        sensor_data = {}
        for sensor in self.config['sensors']:
            sensor_id = sensor['id']
            sensor_type = sensor['type']
            if sensor_type == 'temperature':
                sensor_data[sensor_id] = self.get_temperature_data()
            elif sensor_type == 'vibration':
                sensor_data[sensor_id] = self.get_vibration_data()
            # Add other sensor types as needed
        return sensor_data

    def get_temperature_data(self):
        # Simulate temperature data collection
        return round(random.uniform(20.0, 100.0), 2)

    def get_vibration_data(self):
        # Simulate vibration data collection
        return round(random.uniform(0.0, 10.0), 2)

# Example usage
if __name__ == "__main__":
    collector = SensorDataCollector()
    while True:
        data = collector.collect_data()
        print("Collected Sensor Data:", data)
        time.sleep(5)  # Collect data every 5 seconds
