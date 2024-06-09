# ar_assembly_guide.py
"""
AR-assisted assembly guide script.
"""

import time

class ARAssemblyGuide:
    def __init__(self):
        self.steps = []

    def add_step(self, description, duration):
        self.steps.append({"description": description, "duration": duration})

    def start_guide(self):
        for step in self.steps:
            print(f"Step: {step['description']}")
            time.sleep(step['duration'])
            print(f"Completed: {step['description']}")

# Example usage
if __name__ == "__main__":
    guide = ARAssemblyGuide()
    
    # Add assembly steps
    guide.add_step("Attach part A to part B", 5)
    guide.add_step("Screw part C into part B", 3)
    guide.add_step("Connect the wiring", 7)
    
    # Start the AR assembly guide
    guide.start_guide()
